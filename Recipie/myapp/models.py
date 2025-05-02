from django.db import models

# Create your models here.
class recipie_tbl(models.Model):
    name=models.CharField(max_length=45)
    desc=models.CharField(max_length=250)
    ingre=models.CharField(max_length=150)
    img=models.FileField(upload_to='image')
    instr=models.CharField(max_length=250)
    