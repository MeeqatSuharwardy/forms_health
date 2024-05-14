import json
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import HIPAAAgreement
from django.core.files.base import ContentFile

@csrf_exempt
def submit_hipaa_agreement(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            # Decode and save the signature image
            format, imgstr = data['signatureImageData'].split(';base64,')
            ext = format.split('/')[-1]
            image_file = ContentFile(base64.b64decode(imgstr), name=f"{data['employeeName']}_signature.{ext}")

            # Create and save the HIPAA agreement model instance
            agreement = HIPAAAgreement(
                employee_name=data['employeeName'],
                agreement_date=data['agreementDate'],
                agreement_month=data['agreementMonth'],
                agreement_year=data['agreementYear'],
            )
            agreement.signature_image.save(name=f"{data['employeeName']}_signature.{ext}", content=image_file)
            agreement.save()

            # Generate and save the PDF
            html_content = render_to_string('pdf_templates/pdf_hippa_agreement.html', {
                'agreementDate': agreement.agreement_date,
                'agreementMonth': agreement.agreement_month,
                'agreementYear': agreement.agreement_year,
                'employeeName': agreement.employee_name,
                'signature_image_path': agreement.signature_image.url if agreement.signature_image else None,
            })
            pdf_file_path = f'media/hippa_agreement/{agreement.employee_name}_{agreement.agreement_date}.pdf'
            HTML(string=html_content).write_pdf(pdf_file_path)
            agreement.pdf_file.save(name=f"{agreement.employee_name}_{agreement.agreement_date}.pdf", content=ContentFile(open(pdf_file_path, 'rb').read()))

            return JsonResponse({'status': 'success', 'message': 'HIPAA agreement submitted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def search_hipaa_agreements(request):
    employee_name = request.GET.get('employeeName')
    query = HIPAAAgreement.objects.all()

    if not employee_name:
        return JsonResponse({'error': 'Missing parameter: employeeName is required'}, status=400)

    query = query.filter(employee_name__icontains=employee_name)

    # Define the base URL manually if necessary
    base_url = 'http://127.0.0.1:8000'  # Adjust based on your deployment settings

    data = [
        {
            'employee_name': agreement.employee_name,
            'agreement_date': str(agreement.agreement_date),
            'agreement_month': agreement.agreement_month,
            'agreement_year': agreement.agreement_year,
            'pdf_url': f"{base_url}/{agreement.pdf_file.name}"
        }
        for agreement in query
    ]
    return JsonResponse({'agreements': data}, status=200)