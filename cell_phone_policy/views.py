# views.py
import base64
from django.http import JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import os
from .models import CellPhonePolicyRecord
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.core.files.base import ContentFile
from django.conf import settings

@csrf_exempt
def submit_cell_phone_policy_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        printed_name = data.get('printedName')
        date_of_birth = datetime.strptime(data.get("dateOfBirth"), "%Y-%m-%d").date()
        signature_data = data.get('signature')
        date = datetime.strptime(data.get('date'), "%Y-%m-%d").date()
        logo_path = os.path.join(settings.MEDIA_ROOT, 'logo', 'psychiatry_logo.png')

        if not signature_data:
            return JsonResponse({'status': 'error', 'message': 'Signature data is missing'}, status=400)

        format, imgstr = signature_data.split(';base64,')
        ext = format.split('/')[-1]
        file_name = f'signatures/{printed_name}_{date}.{ext}'
        signature_image_file = ContentFile(base64.b64decode(imgstr), name=file_name)

        record = CellPhonePolicyRecord(
            printed_name=printed_name,
            date_of_birth=date_of_birth,
            submission_date=date,
        )
        record.signature_image.save(file_name, signature_image_file, save=True)
        signature_image_path = os.path.join(settings.MEDIA_ROOT, record.signature_image.name)
        if os.path.exists(signature_image_path):
            print(f"Signature image is confirmed at {signature_image_path}")
        else:
            print("Signature image file does not exist.")

        html_content = render_to_string('pdf_templates/pdf_Cell_Phone_policy.html', {
            'printedName': printed_name,
            'dateOfBirth': date_of_birth,
            'agreementDate': date,
            'signature_image_path': os.path.join(settings.MEDIA_URL, file_name),
            'logo_path': logo_path
        })

        pdf_file_path = f'media/cell_phone_policy/{printed_name}_{date}_{date_of_birth}.pdf'
        HTML(string=html_content).write_pdf(pdf_file_path)

        record.pdf_file = pdf_file_path
        record.save()

        return JsonResponse({'status': 'success', 'message': 'Form submitted successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def search_cell_phone_policy_records(request):
    printed_name = request.GET.get('printedName')
    date_of_birth = request.GET.get('dateOfBirth')
    query = CellPhonePolicyRecord.objects.all()

    if printed_name:
        query = query.filter(printed_name__icontains=printed_name)
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
            'printed_name': record.printed_name,
            'date_of_birth': record.date_of_birth.strftime('%Y-%m-%d'),
            'submission_date': record.submission_date.strftime('%Y-%m-%d'),
            'pdf_url': f"{base_url}/{record.pdf_file.name}"
        }
        for record in query
    ]
    return JsonResponse({'records': data}, status=200)
