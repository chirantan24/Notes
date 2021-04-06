from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    writer=models.ForeignKey(User,null=True,on_delete=models.CASCADE);
    title=models.CharField(max_length=200,null=True);
    text=models.CharField(max_length=1000);
    time_created=models.DateTimeField(null=True);
# Create your models here.
