from django.http import JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import json
from datetime import datetime
from .models import EmploymentApplication, WorkHistory, Qualification, Reference
from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def submit_employment_application(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        logo_path = os.path.join(settings.MEDIA_ROOT, 'logo', 'psychiatry_logo.png')
        application = EmploymentApplication(
            position_applying_for=data['positionApplyingFor'],
            name=data['name'],
            address=data['address'],
            city=data['city'],
            state=data['state'],
            zip=data['zip'],
            home_telephone=data['homeTelephone'],
            business_telephone=data['businessTelephone'],
            cellular=data['cellular'],
            start_date=datetime.strptime(data['startDate'], "%Y-%m-%d").date(),
            salary_desired=data['salaryDesired'],
            hours="".join(data['hours']),
            days="".join(data['days']),
            authorized=data['authorized'],
            special_skills=data['specialSkills'],
            date_of_birth=datetime.strptime(data['dateofbirth'], "%Y-%m-%d").date()
        )
        application.save()

        # Process Work History
        for job in data.get('workHistory', []):
            WorkHistory.objects.create(
                application=application,
                job_title=job['jobTitle'],
                start_date=datetime.strptime(job['startDate'], "%Y-%m-%d").date(),
                end_date=datetime.strptime(job['endDate'], "%Y-%m-%d").date() if job['endDate'] else None,
                company_name=job['companyName'],
                supervisor_name=job['supervisorName'],
                phone_number=job['phoneNumber'],
                city=job['city'],
                state=job['state'],
                zip=job['zip'],
                duties=job['duties'],
                reason_for_leaving=job['reasonForLeaving'],
                starting_salary=job['startingSalary'],
                ending_salary=job['endingSalary'],
            )

        # Process Qualifications
        for qual in data.get('qualifications', []):
            Qualification.objects.create(
                application=application,
                school_name=qual['schoolName'],
                degree=qual['degree'],
            )
        for ref in data.get('references', []):
            Reference.objects.create(
                application=application,
                name=ref['name'],
                phone=ref['phone'],
                relationship=ref['relationship']
            )
        # Generate PDF
        html_content = render_to_string('pdf_templates/pdf_Application_for_employment.html', {
            'application': application,
            'logo_path': logo_path  # Correctly passed here
        })
        pdf_file_path = f'media/application_for_employment/{application.name}_{application.start_date}.pdf'
        HTML(string=html_content).write_pdf(pdf_file_path)

        application.pdf_file = pdf_file_path
        application.save()

        return JsonResponse({'status': 'success', 'message': 'Application submitted successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def search_employment_applications(request):
    position = request.GET.get('position')
    name = request.GET.get('name')
    date_of_birth = request.GET.get('dateOfBirth')
    query = EmploymentApplication.objects.all()

    if position:
        query = query.filter(position_applying_for__icontains=position)
    if name:
        query = query.filter(name__icontains=name)
    if date_of_birth:
        try:
            parsed_date = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
            query = query.filter(date_of_birth=parsed_date)
        except ValueError:
            return JsonResponse({'error': 'Invalid date format'}, status=400)

    # Define the base URL manually if necessary
    base_url = 'http://127.0.0.1:8000'  # Adjust based on your deployment settings

    data = [
        {
            'name': app.name,
            'position_applying_for': app.position_applying_for,
            'date_of_birth': str(app.date_of_birth),
            'pdf_url': f"{base_url}/{app.pdf_file.name}"
        }
        for app in query
    ]
    return JsonResponse({'applications': data}, status=200)