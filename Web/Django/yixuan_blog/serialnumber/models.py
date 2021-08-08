from django.db import models

# Create your models here.

''' table serialnumber '''


class SerialNumber(models.Model):
    id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=25)
    video_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)
    video_tag = models.CharField(max_length=25)
    publish_date = models.DateField()
    video_ticket = models.IntegerField()
    magnet_url = models.CharField(max_length=255)
