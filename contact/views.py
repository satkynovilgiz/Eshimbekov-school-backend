from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json

@csrf_exempt
def send_contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not (name and email and message):
                return JsonResponse({'error': 'Заполните все поля'}, status=400)

            send_mail(
                subject=f'Новое сообщение от {name}',
                message=f'Почта: {email}\n\nСообщение:\n{message}',
                from_email='ilgizzsatkynov@gmail.com',
                recipient_list=['ilgizzsatkynov@gmail.com'],
            )
            return JsonResponse({'success': 'Сообщение отправлено'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Неверный метод'}, status=405)
