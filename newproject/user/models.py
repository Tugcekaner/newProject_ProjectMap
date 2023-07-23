from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
   user = models.OneToOneField(User,verbose_name=("Kulanıcı"), on_delete=models.CASCADE)
   password = models.CharField(("Şifre"), max_length=50,null=True, blank=True)

   class Meta:
      verbose_name_plural = 'Kullanıcı Bilgileri'   

   
   def __str__(self):  
      return self.user.username
