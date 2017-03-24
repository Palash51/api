from rest_framework import serializers
from models import Cars,User_info,Parking_lot,Transaction_info


class User_infoSerializer(serializers.ModelSerializer):
	class Meta:
		model = User_info
		fields = ('id', 'username','birth_date','legal_id','resource','contact')


class CarsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cars
		fields = ('id', 'plate_no','model_name')


class Parking_lotSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parking_lot
		fields = ('id', 'place_name','lot_id','lot_address')

class Transaction_infoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction_info
		fields = ('id', 'username','plot_id','plate_no','check_in_time','check_out_time','amount','flag')
