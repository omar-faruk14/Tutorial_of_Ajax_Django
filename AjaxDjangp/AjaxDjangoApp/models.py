from django.db.models import Model, EmailField, IntegerField, CharField

class AjaxCrud(Model):
    Email = EmailField()
    Password = IntegerField()
    PhoneNumber = CharField(max_length=20)


