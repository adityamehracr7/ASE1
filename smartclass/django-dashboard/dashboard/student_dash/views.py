from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import table, examtype
from .serializers import tableSerializer



class Attendence_data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
  #       data = [
  
  # {
  #   "SID": 418,
  #   "GradeID": "G-07",
  #   "SectionID": "B",
  #   "Topic": "Biology",
  #   "Semester": "F",
  #   "raisedhands": 88,
  #   "VisITedResources": 90,
  #   "AnnouncementsView": 76,
  #   "Discussion": 81,
  #   "StudentAbsenceDays": "Under-7",
  #   "Class": "H"
  # }
# # ]
# {
        # "course_id": "bio",
        # "proff_id": 1,
        # "student_id": "12",
        # "marks": "20",
        # "student_name": "sid",
        # "exam": {
            # "max_marks": "100",
            # "exam_type": "2"
        # },
        # "attendence": {
            # "attendence": "Under7"
        # }

      tablelog= table.objects.all()
      serializer = tableSerializer(tablelog, many=True)
      return Response(serializer.data)

    # def post(self, request):
    #   serializer = tableSerializer(data=request.data)
    #   if serializer.is_valid(raise_exception=True):
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

def prof_dashboard(request):
    return render(request, 'dc/dashboard.html')
