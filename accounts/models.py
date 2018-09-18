from django.conf import settings 
from django.db import models

# Create your models here.

import braintree 


if settings.DEBUG:
        braintree.Configuration.configure(braintree.Environment.Production,
      merchant_id=settings.BRAINTREE_MERCHANT_ID,
      public_key=settings.BRAINTREE_PUBLIC,
      private_key=settings.BRAINTREE_PRIVATE) 


class UserBraintree(models.Model): 
	user = models.OneToOneField(settings.AUTH_USER_MODEL) 
	braintree_id = models.CharField(max_length=120) 

	def __unicode__(self): 
		return str(self.braintree_id) 