from django.db import models

# Create your models here.

class User(AbstractUser):
    gender_choice = (
        ('male', 'male'),
        ('female', 'female'),
    )

    group_choice = (
        ('chef', '요리사'),
        ('housewife', '주부')
    )

    profile_name = models.CharField(max_length=80)
    profile_image = models.ImageField(upload_to='image/profile_image', blank=True)
    gender = models.CharField(max_length=20, choices=gender_choice)
    group = models.CharField(max_length=100, choices=group_choice)
    pass