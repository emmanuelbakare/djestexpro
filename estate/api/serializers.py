from rest_framework import serializers
from estate.models import Estate
from accounts.api.serializers import AccountSerializer


class EstateSerializer(serializers.ModelSerializer):
    # admin = AccountSerializer(many=True, read_only=False)
    # admin=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Estate
        # fields = (  'id', 
        #             'name',
        #             'total_house',
        #             'street1',
        #             'city',
        #             'state_region',
        #             'country',
        #             'admin', 
        #             'comment',)
        # extra_kwargs = {
        #     'admin':{'read_only':True, },
        # }
        # depth:1
        fields = "__all__"

    def create(self, validated_data):
        # validate_data contains all in the information in the form
        # to create an Estate you dont need a admin, so pop admin from the dictionary of data in validate_data
        admins=validated_data.pop('admin')
        # create Estate without adding admin
        estate=Estate.objects.create(**validated_data)

        # to create a many to many relationship you will do estate.admin.add(admin)
        # loop through each admin and it to estate.
        for admin in admins:
            estate.admin.add(admin)
        return estate
        
