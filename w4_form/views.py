from django.http import JsonResponse
from .models import UserW4
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_w4(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        dob = request.POST.get('date_of_birth')
        submitted_year = request.POST.get('submitted_year')
        pdf_data = request.FILES.get('pdf_file')

        if not pdf_data:
            return JsonResponse({'status': 'failed', 'error': 'No PDF file found.'})

        w4_instance = UserW4(full_name=full_name, date_of_birth=dob, pdf_file=pdf_data, submitted_year=submitted_year)
        w4_instance.save()
        return JsonResponse({'status': 'success', 'path': w4_instance.pdf_file.url})

    return JsonResponse({'status': 'failed'})
