from django.shortcuts import render
from django.http import HttpResponse
from AjaxDjangoApp.models import AjaxCrud
from django.views.generic import ListView,DeleteView,View



def home(request):
    return render(request,"index.html")
class HomeCrued(ListView):
    template_name="index.html"
    model=AjaxCrud
    context_object_name="UserData"
class UserInfoSave(View):
    def get(self,request):
        UserEmail=request.Get.get('UserEmail')
        UserPass=request.Get.get('UserPass')
        PhoneNumber=request.Get.get('PhoneNumber')





