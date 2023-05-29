from django.shortcuts import render
from django.http import HttpResponse
from AjaxDjangoApp.models import AjaxCrud
from django.views.generic import ListView,DeleteView,View
from django.http import JsonResponse


def home(request):
    return render(request,"index.html")
class HomeCrued(ListView):
    template_name="index.html"
    model=AjaxCrud
    context_object_name="UserData"
class UserInfoSave(View):
    def get(self,request):
        UserEmail= request.GET.get('UserEmail')
        UserPass= request.GET.get('UserPass')
        UserNumber= request.GET.get('UserNumber')
        
        userObj=AjaxCrud.objects.create(
            Email = UserEmail,
            Password = UserPass,
            PhoneNumber = UserNumber
        )
        user={
            "ID":userObj.id,"UserEmail":userObj.Email,"UserPass":userObj.Password,"UserNumber":userObj.PhoneNumber

        }
        data={
            "user":user
        }
        return JsonResponse(data)





