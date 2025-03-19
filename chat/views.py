from django.shortcuts import render
from django.http import JsonResponse 
from .models import Message 
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def send_message(request):
    if request.method =='POST':
        data = json.loads(request.body)

        username = data.get('username')
        message = data.get('message')

        message = Message.objects.create(username = username, message = message)

        return JsonResponse({'status': 'success','message': 'Message sent Successfully!'})
    return JsonResponse({'status':'error','message':'Invalid request',status:400})


def receive_message(request):
    
    message = Message.objects.all().order_by('timestamp')
    
    message_list = [{'user_name':msg.username,'message':msg.message,'timestamp':msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for msg in message]

    return JsonResponse({'messages':message_list})


def chat_interface(request):
    return render(request,'chat_interface.html')