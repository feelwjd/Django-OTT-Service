from django.conf import settings
from django.db import models


# Create your models here.
class StreammingNvideo(models.Model):
    nvideo = models.FileField(upload_to='videos/', null=True, verbose_name="")
    nid = models.IntegerField(primary_key=True)
    nimage = models.ImageField(upload_to='images/',null=True, verbose_name="")
    class Meta:
        managed = False
        db_table = 'streamming_nvideo' 
        

    def __str__(self):
        return str(self.nvideo)

class Checkout(models.Model):
    user_id = models.TextField()
    nid = models.IntegerField()
    num = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'checkout'

    def __str__(self):
        return str(self.user_id)