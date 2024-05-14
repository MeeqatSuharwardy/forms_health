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


def search_w4_forms(request):
    full_name = request.GET.get('full_name')
    date_of_birth = request.GET.get('date_of_birth')
    submitted_year = request.GET.get('submitted_year')
    query = UserW4.objects.all()

    if not full_name or not date_of_birth:
        return JsonResponse({'error': 'Missing parameters: full_name and date_of_birth are required'}, status=400)

    query = query.filter(full_name__icontains=full_name, date_of_birth=date_of_birth)

    if submitted_year:
        query = query.filter(submitted_year=submitted_year)

    # Define the base URL manually if necessary
    base_url = 'http://127.0.0.1:8000'  # Adjust based on your deployment settings

    data = [
        {
            'full_name': w4.full_name,
            'date_of_birth': w4.date_of_birth,
            'submitted_year': w4.submitted_year,
            'pdf_url': f"{base_url}/{w4.pdf_file.name}"
        }
        for w4 in query
    ]
    return JsonResponse({'forms': data}, status=200)