import json
from django.shortcuts import render,redirect
from .models import SurveyPhase1,SurveyPhase2,SurveyPhase3
from login import views as login_app_view

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def createSurvey(request):
    jsonData = json.loads(request.body)
    name = jsonData.get('patientName')
    surveyType = jsonData.get('surveyType')
    print(name)
    print(surveyType)

    if surveyType == 'On Addmission':
        age = jsonData.get('age')
        gender = jsonData.get('gender')
        location = jsonData.get('location')
        phone = jsonData.get('phoneNumber')
        source = jsonData.get('hospitalSource'),
        whyRkhc = jsonData.get('whyRkhc')
        anyIssue = jsonData.get('issueWithFindingRkch')
        anyIssueReason = jsonData.get('issueWithFindingRkchReason')
        regExp = jsonData.get('experienceInReg')
        regExpReason = jsonData.get('experienceInRegReason')
        admExp = jsonData.get('experienceInAdmission')
        admExpReason = jsonData.get('experienceInAdmissionReason')
        parkExp = jsonData.get('parking')
        parkExpReason = jsonData.get('parkingReason')
        financeExp = jsonData.get('finance')
        financeExpReason = jsonData.get('financeReason')
        createdBy = jsonData.get('createdBy')
        SurveyPhase1.objects.create(patientName=name,patientAge=age,gender=gender,patientOrigin=location,phoneNumber=phone,hospitalSource=source,whyRkch=whyRkhc,issueWithFindingRkch=anyIssue,issueWithFindingRkchReason=anyIssueReason,experienceInReg=regExp,experienceInRegReason=regExpReason,experienceInAdmission=admExp,experienceInAdmissionReason=admExpReason,parking=parkExp,parkingReason=parkExpReason,finance=financeExp,financeReason=financeExpReason,createdBy=createdBy)
        return JsonResponse({"status":"success"})

    elif surveyType == 'During Addmission':
        doctor = jsonData.get('doctor')
        doctorReason = jsonData.get('doctorReason')
        staff =jsonData.get('staff')
        staffReason = jsonData.get('staffReason')
        tests = jsonData.get('tests')
        testsReason = jsonData.get('testsReason')
        createdBy = jsonData.get('createdBy')
        SurveyPhase2.objects.create(patientName=name,doctor=doctor,doctorReason=doctorReason,staff=staff,staffReason=staffReason,tests=tests,testsReason=testsReason,createdBy=createdBy)
        return JsonResponse({"status":"success"})

    elif surveyType == 'After Addmission':
        discharge = jsonData.get('discharge')
        dischargeReason = jsonData.get('dischargeReason')
        billing = jsonData.get('billing')
        billingReason = jsonData.get('billingReason')
        continuum = jsonData.get('continuum')
        continuumReason = jsonData.get('continuumReason')
        createdBy = jsonData.get('createdBy')
        SurveyPhase3.objects.create(patientName=name,discharge=discharge,dischargeReason=dischargeReason,billing=billing,billingReason=billingReason,continuum=continuum,continuumReason=continuumReason,createdBy=createdBy)

        return JsonResponse({"status":"success"})
    
    else:
        return JsonResponse({"status":"error"})


def dashboard(request):
    if request.session.get("email") and request.session.get("name"):
        survey1 = SurveyPhase1.objects.all()
        survey2 = SurveyPhase2.objects.all()
        survey3 = SurveyPhase3.objects.all()
        return render(request,'home.html',{'surveyData1':survey1,'surveyData2':survey2,'surveyData3':survey3})
    else:
        return redirect(login_app_view.login_staff)