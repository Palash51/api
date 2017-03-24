from django.contrib import admin
from . import models
from models import Cars,User_info,Parking_lot,Transaction_info
# Register your models here.
admin.site.register(Cars)
admin.site.register(User_info)
admin.site.register(Parking_lot)
admin.site.register(Transaction_info)
