from django.db import models

# Create your models here.
class SurveyPhase1(models.Model):
    patientName = models.CharField(max_length=1000,default='')
    patientAge = models.IntegerField(default=0)
    gender = models.CharField(max_length=10,default='')
    patientOrigin = models.CharField(max_length=1000,default='')
    phoneNumber = models.CharField(max_length=1000,default='')
    hospitalSource = models.CharField(max_length=1000,default='')
    whyRkch = models.CharField(max_length=1000,default='')
    issueWithFindingRkch = models.CharField(max_length=1000,default='')
    issueWithFindingRkchReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    experienceInReg = models.CharField(max_length=1000,default='')
    experienceInRegReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    experienceInAdmission=models.CharField(max_length=1000,default='')
    experienceInAdmissionReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    parking = models.CharField(max_length=1000,default='')
    parkingReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    finance = models.CharField(max_length=1000,default='')
    financeReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    createdBy = models.CharField(max_length=100,default='')

class SurveyPhase2(models.Model):
    patientName = models.CharField(max_length=1000,default='')
    doctor = models.CharField(max_length=1000,default='')
    doctorReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    staff = models.CharField(max_length=1000,default='')
    staffReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    tests = models.CharField(max_length=1000,default='')
    testsReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    createdBy = models.CharField(max_length=100,default='')


class SurveyPhase3(models.Model):
    patientName = models.CharField(max_length=1000,default='')
    discharge = models.CharField(max_length=1000,default='')
    dischargeReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    billing = models.CharField(max_length=1000,default='')
    billingReason= models.CharField(max_length=1000,default='',blank=True,null=True)
    continuum = models.CharField(max_length=1000,default='')
    continuumReason = models.CharField(max_length=1000,default='',blank=True,null=True)
    createdBy = models.CharField(max_length=100,default='')