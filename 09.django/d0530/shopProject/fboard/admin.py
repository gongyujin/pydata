from django.contrib import admin
from fboard.models import Fboard



@admin.register(Fboard)
class FboardAmin(admin.ModelAdmin):
    list_display=['f_no','f_title','member','f_updatedate']