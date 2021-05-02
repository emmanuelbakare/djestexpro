from rest_framework import serializers
from resident.models import Resident
from accounts.api.serializers import AccountSerializer
from estate.api.serializers import EstateSerializer


class ResidentSerializer(serializers.ModelSerializer):
    # admin = AccountSerializer(many=True, read_only=False)
    # admin=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user=serializers.StringRelatedField()
    # estate=serializers.HyperlinkedRelatedField(many=True,view_name='estate', read_only=True)
    # estate= EstateSerializer(many=True)
    class Meta:
        model = Resident
        fields = "__all__"
        fields= ('user', 'house_address','created_date', 'estate')

    
