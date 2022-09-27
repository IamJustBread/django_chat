from PIL import Image
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужчина'),
        ('F', 'Женщина'),
        ('NS', 'Не указано'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='')
    date_of_birth = models.DateField(default='1990-01-01')
    gender = models.CharField(default='NS', choices=GENDER_CHOICES, max_length=4)

    def __str__(self):
        return f'{self.user.username} Profile'
