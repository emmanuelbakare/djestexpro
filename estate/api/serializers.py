from rest_framework import serializers 
from rest_framework.response import Response
from estate.models import Estate, EstateAdmin, EstateType
from accounts.api.serializers import AccountSerializer


class EstateAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateAdmin
        fields="__all__"

     
    
 

class EstateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateType
        fields = "__all__"

class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = "__all__"

class EstateResidentSerializer(serializers.ModelSerializer):
    # admins=serializers.SerializerMethodField()
    class Meta:
        model = Estate
        fields="__all__"
        # fields= ['name','total_house', 'estate_type','street1',
        #          'city','state_region','country','status','comment',
        #          'created_date', 'admins'

        #   
   
 
    # def get_admins(self, obj):
    #     # admins=EstateAdmin.objects.filter(estate=obj)
    #     admins=EstateAdmin.objects.filter(estate=obj)
    #     adminSerializer=EstateAdminSerializer(admins, many=True)
    #     # return Response(adminSerializer.data)
    #     return adminSerializer.data
    
    # def create(self,validated_data):
    #     users=validated_data.pop('account')
    #     resident=validated_data.pop('resident')
    #     print('USER INFO ', users)
    #     print('RESIDENT INFO', resident)
    #     print('OTHER DATA - ESTATE ', **validated_data)



    # def create(self,validated_data):
    #     print('VALIDATED DATA : ',validated_data)
    #     adminID=validated_data.pop('admin')
    #     print('admin ID ', adminID)
    #     estate=Estate.objects.create(**validated_data)
    #     estate.admins.create(user_id=adminID)

    #     return estate


    # def create(self, validated_data):
    #     # validate_data contains all in the information in the form
    #     # to create an Estate you dont need a admin, so pop admin from the dictionary of data in validate_data
        # admins=validated_data.pop('admin')
    #     # create Estate without adding admin
        # estate=Estate.objects.create(**validated_data)

        

    #     # to create a many to many relationship you will do estate.admin.add(admin)
    #     # loop through each admin and it to estate.
    #     for admin in admins:
    #         estate.admin.add(admin)
    #     return estate
        
