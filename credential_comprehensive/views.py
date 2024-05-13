import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CredentialApplication
from django.core.files.base import ContentFile

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
