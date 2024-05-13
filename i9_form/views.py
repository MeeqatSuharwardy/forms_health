from django.http import JsonResponse
from .models import UserPDF
from django.views.decorators.csrf import csrf_exempt
import base64

@csrf_exempt
def upload_pdf(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        dob = request.POST.get('date_of_birth')
        submitted_year = request.POST.get('submitted_year')
        pdf_data = request.FILES.get('pdf_file')

        if not pdf_data:
            return JsonResponse({'status': 'failed', 'error': 'No PDF file found.'})

        pdf_instance = UserPDF(full_name=full_name, date_of_birth=dob, pdf_file=pdf_data, submitted_year=submitted_year)
        pdf_instance.save()
        return JsonResponse({'status': 'success', 'path': pdf_instance.pdf_file.url})
    else:
        # Handle GET for search
        full_name = request.GET.get('full_name')
        dob = request.GET.get('date_of_birth')
        year = request.GET.get('year')
        results = UserPDF.objects.filter(full_name__icontains=full_name, date_of_birth=dob, submitted_year=year)
        data = [{"full_name": obj.full_name, "dob": obj.date_of_birth, "year": obj.submitted_year, "pdf_url": obj.pdf_file.url} for obj in results]
        return JsonResponse(data, safe=False)

    return JsonResponse({'status': 'failed'})
