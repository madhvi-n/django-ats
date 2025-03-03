from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from core.models import TimeStampedModel


class Candidate(TimeStampedModel):
    class GenderChoices(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        OTHER = "Other", "Other"

    name = models.CharField(max_length=255, db_index=True)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(100)]
    )
    gender = models.CharField(max_length=10, choices=GenderChoices, db_index=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(r"^\+?\d{7,15}$", "Enter a valid phone number.")],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["email", "phone_number"], name="unique_candidate_email_phone"),
        ]
        ordering = ["name"]

    def __str__(self):
        return self.name
