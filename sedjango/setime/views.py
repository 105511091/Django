from django.shortcuts import render

# Create your views here.
from .models import Message

def time(request):
    if 'cuName' in request.POST:
        cuName = request.POST['cuName']
        email = request.POST['email']
        question = request.POST['question']
        content = request.POST['content']
        
        obj=Message.objects.create(name=cuName,email=email,subject=question,content=content)
        
        obj.save()
        
        
    return render(request,'time.html',locals())