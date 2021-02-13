from django.contrib import admin
from app1.models import MembersModel

# Register your models here.
@admin.register(MembersModel)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['idno','real_name','timezone','start_time_one','end_time_one','start_time_two','end_time_two','start_time_three','end_time_three']