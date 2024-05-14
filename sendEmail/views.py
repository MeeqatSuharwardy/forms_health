# views.py
from django.core.mail import EmailMessage
from django.http import JsonResponse
from rest_framework.decorators import api_view
import os

@api_view(['POST'])
def send_email(request):
    email = request.data.get('email')
    subject = request.data.get('subject')
    message = request.data.get('message')
    filenames = request.data.get('filenames')
    user = request.data.get('user')
    password = request.data.get('password')

    if not email or not subject or not message or not filenames or not user or not password:
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    try:
        # Using win32com.client to send email via Windows Authentication
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = email
        mail.Subject = subject
        mail.Body = message

        for filename in filenames:
            file_path = os.path.join('src', 'components', 'Forms', 'new_forms', filename)
            if os.path.exists(file_path):
                mail.Attachments.Add(file_path)
            else:
                return JsonResponse({'error': f'File {filename} not found'}, status=404)

        mail.Send()
        return JsonResponse({'success': 'Email sent successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)