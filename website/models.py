from django.db import models

# Create your models here.
class ContactData(models.Model):
  name = models.CharField(max_length=50, blank = True, null = True)
  email_id = models.EmailField(max_length=254)
  message = models.TextField(max_length=1000, blank = True, null = True)
  subject = models.CharField(max_length=250, blank = True, null = True)
  
  def __str__(self):
      return self.name
  
  



