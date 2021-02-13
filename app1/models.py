from django.db import models

class MembersModel(models.Model):
    idno = models.CharField(max_length=50,primary_key=True)
    real_name=models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)
    start_time_one = models.DateTimeField()
    end_time_one = models.DateTimeField()
    start_time_two = models.DateTimeField()
    end_time_two = models.DateTimeField()
    start_time_three = models.DateTimeField()
    end_time_three = models.DateTimeField()


