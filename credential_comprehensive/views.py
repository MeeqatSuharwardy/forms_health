import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CredentialApplication
from django.core.files.base import ContentFile
from datetime import datetime

@csrf_exempt
def submit_credential_application(request):
    if request.method == 'POST':
        data = request.FILES or json.loads(request.body)
        application = CredentialApplication(
            caqh_id=data.get('caqhId'),
            caqh_login=data.get('caqhLogin'),
            caqh_password=data.get('caqhPassword'),
            npi_registration=data.get('npireg'),
            npi_number=data.get('npiNumber'),
            npi_password=data.get('npiPassword'),
            full_name=data.get('fullName'),
            ssn=data.get('ssn'),
            phone_number=data.get('phoneNumber'),
            date_of_birth=data.get('dob'),
            place_of_birth=data.get('pob'),
            home_address=data.get('homeAddress'),
            email=data.get('email'),
            specialty=data.get('specialty'),
            taxonomy=data.get('taxonomy'),
            fl_license_number=data.get('flLicenseNumber'),
            document_type=data.get('documentType'),
            document=request.FILES.get('fileUpload'),
            reason_if_no_document=data.get('reasonIfNoDocument')
        )
        application.save()

        return JsonResponse({'status': 'success', 'message': 'Application submitted successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def search_credential_applications(request):
    full_name = request.GET.get('fullName')
    date_of_birth = request.GET.get('dateOfBirth')
    query = CredentialApplication.objects.all()

    if full_name:
        query = query.filter(full_name__icontains=full_name)
    if date_of_birth:
        try:
            dob_date = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
            query = query.filter(date_of_birth=dob_date)
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Please use YYYY-MM-DD format.'}, status=400)

    # Define the base URL manually if necessary
    base_url = 'http://127.0.0.1:8000'  # Adjust based on your deployment settings

    data = [
        {
            'full_name': application.full_name,
            'date_of_birth': application.date_of_birth.strftime('%Y-%m-%d'),
            'submission_date': application.submission_date.strftime('%Y-%m-%d'),
            'pdf_url': f"{base_url}/{application.document.name}"
        }
        for application in query
    ]
    return JsonResponse({'applications': data}, status=200)