from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from htmlmin.decorators import minified_response
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import TaskSerializer
from django.contrib.auth.models import User

# class Test(APIView):

#     def get(self, request, id, format=None):

#         task = Taks.objects.get(id=id)

#         serializer = TaskSerializer(task)

#         return JsonResponse({status: 'success'})
