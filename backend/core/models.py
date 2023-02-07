from django.db import models
from django.contrib.auth.models import User
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

# Create your models here.

class Product(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):


	class Meta:
		verbose_name_plural = "Product"
		verbose_name_plural = 'Products'


	def __str__(self):
		return f'{self.title}'
