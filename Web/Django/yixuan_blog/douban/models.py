from django.db import models

# Create your models here.
class FilmDetail(models.Model):
    film_id = models.CharField(primary_key=True, max_length=25)
    film_title = models.CharField(max_length=25, null=True)
    film_rate = models.DecimalField(max_length=25, max_digits=2, decimal_places=1, null=True)
    positive_emotion = models.IntegerField(null=True)
    negative_emotion = models.IntegerField(null=True)
    total_score = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    film_result = models.CharField(max_length=25, null=True)


class FilmReview(models.Model):
    film_id = models.CharField(max_length=25, null=True)
    film_review = models.TextField(max_length=0, null=True)
    film_review_up = models.IntegerField(null=True)
    film_review_user = models.CharField(max_length=25, null=True)
    film_review_date = models.DateField(null=True)
