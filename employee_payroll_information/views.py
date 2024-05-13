from django.http import JsonResponse
from .models import EmployeePayroll
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from weasyprint import HTML
import json
import base64
from django.core.files.base import ContentFile

@csrf_exempt
def submit_employee_payroll(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            payroll = EmployeePayroll(
                employee_name=data['employeeName'],
                date_of_hire=data['dateOfHire'],
                original_position=data['originalPosition'],
                change_position_date=data['changePositionDate'],
                pay_type=data['payType'],
                pay_frequency=data['payFrequency'],
                hire_pay_rate=data['hirePayRate'],
                effective_date=data['effectiveDate'],
                approval_date=data['approvalDate'],
                date_signed=data['dateSigned']
            )

            if 'signature' in data:
                format, imgstr = data['signature'].split(';base64,')
                ext = format.split('/')[-1]
                image_file = ContentFile(base64.b64decode(imgstr), name=f"{payroll.employee_name}_signature.{ext}")
                payroll.signature_image.save(name=f"{payroll.employee_name}_signature.{ext}", content=image_file, save=False)

            payroll.save()

            html_content = render_to_string('pdf_templates/pdf_employee_payroll_information.html', {
                'employee_name': payroll.employee_name,
                'date_of_hire': payroll.date_of_hire,
                'original_position': payroll.original_position,
                'change_position_date': payroll.change_position_date,
                'pay_type': payroll.pay_type,
                'pay_frequency': payroll.pay_frequency,
                'hire_pay_rate': payroll.hire_pay_rate,
                'effective_date': payroll.effective_date,
                'approval_date': payroll.approval_date,
                'signature_image_path': payroll.signature_image.url if payroll.signature_image else None,
                'date_signed': payroll.date_signed
            })
            pdf_file_path = f'media/employee_payroll_information/{payroll.employee_name}_{payroll.date_signed}.pdf'
            HTML(string=html_content).write_pdf(pdf_file_path)
            payroll.pdf_file.save(name=f"{payroll.employee_name}_{payroll.date_signed}.pdf", content=ContentFile(open(pdf_file_path, 'rb').read()), save=True)

            return JsonResponse({'status': 'success', 'message': 'Payroll information submitted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
