from django.http import JsonResponse
from .models import DirectDeposit
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from weasyprint import HTML
import json
import base64
from django.core.files.base import ContentFile

@csrf_exempt
def submit_direct_deposit(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parsing JSON data correctly
            direct_deposit = DirectDeposit(
                name=data['name'],
                address=data['address'],
                city_state_zip=data['cityStateZip'],
                bank_name=data['bankName'],
                account_number=data['accountNumber'],
                routing_number=data['routingNumber'],
                amount=data['amount'],
                percentage=data['percentage'],
                account_type=data['accountType'],
                company_name=data['companyName'],
                date=data['date']
            )

            # Handling the signature image
            if 'signatureImage' in data and data['signatureImage']:
                format, imgstr = data['signatureImage'].split(';base64,')
                ext = format.split('/')[-1]  # Extract file extension
                image_file = ContentFile(base64.b64decode(imgstr), name=f"{direct_deposit.name}_signature.{ext}")
                direct_deposit.signature_image.save(name=f"{direct_deposit.name}_signature.{ext}", content=image_file, save=False)

            direct_deposit.save()

            # Generate and save PDF with new template
            html_content = render_to_string('pdf_templates/pdf_direct_deposit_authorization.html', {
                'title': 'DIRECT DEPOSIT AUTHORIZATION',
                'name': direct_deposit.name,
                'address': direct_deposit.address,
                'city_state_zip': direct_deposit.city_state_zip,
                'bankName': direct_deposit.bank_name,
                'accountNumber': direct_deposit.account_number,
                'routing_number': direct_deposit.routing_number,
                'amount': direct_deposit.amount,
                'percentage': direct_deposit.percentage,
                'account_type': direct_deposit.account_type,
                'company_name': direct_deposit.company_name,
                'signature_image_path': direct_deposit.signature_image.url if direct_deposit.signature_image else None,
                'signature_date': direct_deposit.date
            })
            pdf_file_path = f'media/direct_deposit/{direct_deposit.name}_{direct_deposit.date}.pdf'
            HTML(string=html_content).write_pdf(pdf_file_path)
            direct_deposit.pdf_file.save(name=f"{direct_deposit.name}_{direct_deposit.date}.pdf", content=ContentFile(open(pdf_file_path, 'rb').read()), save=True)

            return JsonResponse({'status': 'success', 'message': 'Direct deposit submitted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def search_direct_deposits(request):
    name = request.GET.get('name')
    date = request.GET.get('date')

    if not name or not date:
        return JsonResponse({'error': 'Missing parameters: name and date are required'}, status=400)

    deposits = DirectDeposit.objects.filter(name__icontains=name, date=date)
    if deposits.exists():
        data = [{'name': deposit.name, 'date': str(deposit.date)} for deposit in deposits]
        return JsonResponse({'deposits': data}, status=200)
    else:
        return JsonResponse({'error': 'No deposits found'}, status=404)
