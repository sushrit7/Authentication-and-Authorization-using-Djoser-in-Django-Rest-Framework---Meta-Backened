from rest_framework import serializers 
from .models import Rating 
from rest_framework.validators import UniqueTogetherValidator 
from django.contrib.auth.models import User 
 
 
class RatingSerializer (serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField( 
    queryset=User.objects.all(), 
    default=serializers.CurrentUserDefault() 
    )
    class Meta: 
        model = Rating 
        fields = ('id', 'menuitem_id', 'rating', 'user') 
        validators = [ 
            UniqueTogetherValidator( 
                queryset=Rating.objects.all(), 
                fields=('menuitem_id', 'user') 
            ) 
        ]
        extra_kwargs = {
            'rating' : {'min_value': 0, 'max_value': 5},
        }