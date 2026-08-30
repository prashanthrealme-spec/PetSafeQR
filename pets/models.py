from django.db import models
from django.contrib.auth.models import User
import uuid


class Pet(models.Model):

    PET_TYPES = [
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
        ('BIRD', 'Bird'),
        ('RABBIT', 'Rabbit'),
        ('FISH', 'Fish'),
        ('TURTLE', 'Turtle'),
        ('HAMSTER', 'Hamster'),
        ('OTHER', 'Other'),
    ]

    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]

    STATUS_CHOICES = [
        ('SAFE', 'Safe'),
        ('MISSING', 'Missing'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pets'
    )

    pet_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    name = models.CharField(
        max_length=100
    )

    pet_type = models.CharField(
        max_length=20,
        choices=PET_TYPES
    )

    breed = models.CharField(
        max_length=100,
        blank=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    color = models.CharField(
        max_length=50
    )

    identification_details = models.TextField(
        blank=True
    )

    photo = models.ImageField(
        upload_to='pets/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='SAFE'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name