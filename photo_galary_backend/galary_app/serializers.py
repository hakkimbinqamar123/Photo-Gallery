from rest_framework import serializers
from galary_app.models import *

class GalarySerializers(serializers.ModelSerializer):
    class Meta:
        model=AddPhoto
        fields =(
            'user_id',
            'title',
            'image',
            'description'
        )

class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            'email',
            'password',
            'image',
            'username'
        )
 