import json
from django.shortcuts import render,redirect
from .models import Login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def login(request):
    jsonData = json.loads(request.body)
    email = jsonData.get('email')
    password = jsonData.get('password')
    fromMobile = jsonData.get('fromMobile')
    isUser = Login.objects.filter(email=email,password=password).exists()
    if isUser == True and fromMobile ==True:
        return JsonResponse({"status":"success"})
    elif isUser == True and fromMobile == False:
        if str(email).startswith('admin'):
            return JsonResponse({"status":"successForWeb"})
        else:
            return JsonResponse({"status":"error"})
    else:
        return JsonResponse({"status":"error"})

def logout_staff(request):
    request.session.flush()
    return redirect(login_staff)

def login_staff(request):
    if request.session.get("email") and request.session.get("name"):
        print("Logged in")
        # return JsonResponse({"status":"login"})
        return redirect('home.html')
    else:
        return render(request,'login.html')