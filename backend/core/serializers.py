from . import models
from rest_framework import serializers
from rest_framework.fields import CharField


class ProductSerializer(serializers.ModelSerializer):

	name = CharField(source="title", required=True)
	detail = CharField(source="description", required=True)
	
	class Meta:
		model = models.Product
		fields = (
			'name',
			'detail'
		)

		
