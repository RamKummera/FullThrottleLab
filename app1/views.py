from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework.views import APIView
from app1.models import MembersModel
from django.http import HttpResponse
import json


class EmployeeDetails(APIView):
    def get(self,request):
        data = MembersModel.objects.all()
        dict={"ok": True}
        for x in data:

            d1 = {
                        "id":x.idno,
                        "real_name":x.real_name,
                        "tz": x.timezone,
                        "activity_periods":[
                            {
                                "start_time":x.start_time_one.strftime("%d-%m-%y %I:%M"),
                                "end_time":x.end_time_one.strftime("%d-%m-%y %I:%M")
                            },
                            {
                                "start_time": x.start_time_two.strftime("%d-%m-%y %I:%M"),
                                "end_time": x.end_time_two.strftime("%d-%m-%y %I:%M")
                            },
                            {
                                "start_time": x.start_time_three.strftime("%d-%m-%y %I:%M"),
                                "end_time": x.end_time_three.strftime("%d-%m-%y %I:%M")
                            }
                        ]
                    }
            dict.setdefault('members', []).append(d1)
        js = json.dumps(dict,indent=4)
        return HttpResponse(js,content_type='application/json')


def displayDetails(request):
    return render(request,'display.html')