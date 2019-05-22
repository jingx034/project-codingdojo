from django.shortcuts import HttpResponse
from django.core import serializers
from .models import *

def index(request):
    user = User.objects.all()
    serialized_user = serializers.serialize('json',user)
    return HttpResponse(serialized_user,content_type='application/json',status=200)

# def show(request,user_id):
#     getuser=User.objects.filter(id=user_id)
#     data = serializers.serialize("json",getuser,indent=2,use_natural_foreign_keys=True)
#     return HttpResponse(data, content_type='application/json', status=200)