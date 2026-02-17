from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField


class Level(models.Model):
    """
    Level of difficulty for each Course offered.
    Examples: Beginner, Intermediate, Advanced.
    """
    name = models.CharField(max_length=32, unique=True, null=False, blank=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class SupplyItem(models.Model):
    """
    Items/Supplies a student might need to attend (generic items).
    Examples: tools, spirits, mixers, glassware, garnishes, etc.
    """
    name = models.CharField(max_length=120, unique=True, null=False, blank=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    Different courses offered for purchase.
    """
    level = models.ForeignKey(Level, on_delete=models.PROTECT, related_name="courses")

    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    location = models.CharField(max_length=200, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    image = CloudinaryField('image', blank=True, null=True)

    price = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Price as a whole number."
    )

    max_participants = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        help_text="Maximum number of participants allowed."
    )

    supplies = models.ManyToManyField(
        SupplyItem,
        related_name="courses",
        blank=True,
        help_text="Items students should have before attending."
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["level__name", "name"]

    def __str__(self):
        return self.name
