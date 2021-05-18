from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

import api.models as api_models
from api.serializers import WindTestSerializer, LongRunningTaskSerializer

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'

class WindTest(generics.CreateAPIView):
    serializer_class = WindTestSerializer

    def post(self, request, format=None):
        """
        Return task id of long running task.
        """
        response = {}
        task = api_models.LongRunningTask.objects.create(
            state=api_models.LongRunningTask.PROCESSING_STATE,
        )
        serializer = self.serializer_class(
            data=request.data,
            context={
                'task_id': task.id,
            }
        )
        serializer.is_valid(raise_exception=True)
        task_id, result = serializer.save()
        response['task_id'] = task_id
        response['result'] = result
        return Response(response, status=status.HTTP_200_OK)


class GetResult(generics.RetrieveAPIView):
    """To Update or Delete a single Long Running Task"""
    serializer_class = LongRunningTaskSerializer

    def get_object(self):
        return api_models.LongRunningTask.objects.get(id=self.kwargs['task_id'])
