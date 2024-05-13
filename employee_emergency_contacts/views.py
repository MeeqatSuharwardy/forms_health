from django.http import JsonResponse
from .models import EmergencyContact
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from weasyprint import HTML
import json
import base64
from django.core.files.base import ContentFile

@csrf_exempt
def submit_emergency_contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            emergency_contact = EmergencyContact(
                employee_name=data['employeeName'],
                phone_number=data['phoneNumber'],
                address=data['address'],
                city_state_zip=data['cityStateZip'],
                primary_contact_name=data['primaryName'],
                primary_contact_relationship=data['primaryRelationship'],
                primary_contact_phone=data['primaryPhone'],
                primary_contact_alt_phone=data['primaryAltPhone'],
                secondary_contact_name=data['secondaryName'],
                secondary_contact_relationship=data['secondaryRelationship'],
                secondary_contact_phone=data['secondaryPhone'],
                secondary_contact_alt_phone=data['secondaryAltPhone'],
                doctor_name=data['doctorName'],
                doctor_phone=data['doctorPhone'],
                doctor_address=data['doctorAddress'],
                date_signed=data['dateSigned']
            )

            if 'signatureImage' in data:
                format, imgstr = data['signatureImage'].split(';base64,')
                ext = format.split('/')[-1]
                image_file = ContentFile(base64.b64decode(imgstr), name=f"{emergency_contact.employee_name}_signature.{ext}")
                emergency_contact.signature_image.save(name=f"{emergency_contact.employee_name}_signature.{ext}", content=image_file, save=False)

            emergency_contact.save()

            html_content = render_to_string('pdf_templates/pdf_emergency_contacts_final.html', {
                'employee_name': emergency_contact.employee_name,
                'phone_number': emergency_contact.phone_number,
                'address': emergency_contact.address,
                'city_state_zip': emergency_contact.city_state_zip,
                'primary_contact_name': emergency_contact.primary_contact_name,
                'primary_contact_phone': emergency_contact.primary_contact_phone,
                'secondary_contact_name': emergency_contact.secondary_contact_name,
                'doctor_name': emergency_contact.doctor_name,
                'signature_image_path': emergency_contact.signature_image.url if emergency_contact.signature_image else None,
                'date_signed': emergency_contact.date_signed
            })

            pdf_file_path = f'media/employee_payroll_information/{emergency_contact.employee_name}_{emergency_contact.date_signed}.pdf'
            HTML(string=html_content).write_pdf(pdf_file_path)
            emergency_contact.pdf_file.save(name=f"{emergency_contact.employee_name}_{emergency_contact.date_signed}.pdf", content=ContentFile(open(pdf_file_path, 'rb').read()), save=True)

            return JsonResponse({'status': 'success', 'message': 'Emergency contact information submitted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def search_emergency_contacts(request):
    name = request.GET.get('employee_name')
    date = request.GET.get('date_signed')

    if name and date:
        contacts = EmergencyContact.objects.filter(
            employee_name__icontains=name,
            date_signed=date
        )
        data = [{'employee_name': contact.employee_name, 'date_signed': str(contact.date_signed)} for contact in contacts]
        return JsonResponse({'contacts': data}, status=200)

    return JsonResponse({'error': 'Missing parameters'}, status=400)
