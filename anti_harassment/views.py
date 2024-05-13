import base64
from django.http import JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import os
from .models import AntiHarassmentRecord
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.core.files.base import ContentFile
from django.conf import settings

@csrf_exempt
def submit_anti_harassment_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        printed_name = data.get('printedName')
        date_of_birth = data.get("dateOfBirth")
        signature_data = data.get('signatureImageData')
        logo_path = os.path.join(settings.MEDIA_ROOT, 'logo', 'psychiatry_logo.png')

        date = data.get('date')

        if not signature_data:
            return JsonResponse({'status': 'error', 'message': 'Signature data is missing'}, status=400)

        format, imgstr = signature_data.split(';base64,')
        ext = format.split('/')[-1]
        file_name = f'cell_phone_policy/signatures/{printed_name}_{date}.{ext}'
        signature_image_file = ContentFile(base64.b64decode(imgstr), name=file_name)

        record = AntiHarassmentRecord(
            printed_name=printed_name,
            submission_date=datetime.strptime(date, "%Y-%m-%d").date(),
            date_of_birth = date_of_birth,
        )
        record.signature_image.save(file_name, signature_image_file, save=True)

        # Confirm the image path
        signature_image_path = os.path.join(settings.MEDIA_URL, 'cell_phone_policy/signatures', file_name)

        if os.path.exists(os.path.join(settings.MEDIA_ROOT, 'cell_phone_policy/signatures', file_name)):
            print(f"Signature image is confirmed at {signature_image_path}")
        else:
            print("Signature image file does not exist.")

        html_content = render_to_string('pdf_templates/pdf_anti_harassment_discrimination_final.html', {
            'printedName': printed_name,
            'date_signed': date,
            'signature_image_path': signature_image_path,
            'logo_path': logo_path
        })

        pdf_file_path = f'media/anti_harassment/{printed_name}_{date}.pdf'
        HTML(string=html_content).write_pdf(pdf_file_path)

        record.pdf_file = pdf_file_path
        record.save()

        return JsonResponse({'status': 'success', 'message': 'Form submitted successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def search_anti_harassment_records(request):
    printed_name = request.GET.get('printedName')
    date_of_birth = request.GET.get('dateOfBirth')

    if printed_name and date_of_birth:
        records = AntiHarassmentRecord.objects.filter(
            printed_name__icontains=printed_name,
            date_of_birth=date_of_birth
        )
        data = [
            {
                'printed_name': record.printed_name,
                'date_of_birth': str(record.date_of_birth),
                'submission_date': str(record.submission_date),
                'pdf_file': request.build_absolute_uri(record.pdf_file.url)  # Provide full URL to the PDF file
            } for record in records
        ]
        return JsonResponse({'records': data}, status=200)

    return JsonResponse({'error': 'Missing parameters'}, status=400)