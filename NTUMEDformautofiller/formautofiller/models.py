from django.db import models

# Create your models here.

class Preference(models.Model):
    """Model representing a user preference."""
    SCORE_A = "2"
    SCORE_B = "3"
    SCORE_C = "4"
    SCORE_D = "5"
    SCORE_E = "6"
    SCORE_CHOICES = (
        (SCORE_A, "A: Perfect"),
        (SCORE_B, "B: Good"),
        (SCORE_C, "C: Normal"),
        (SCORE_D, "D: Bad"),
        (SCORE_E, "E: Lame"),
    )
    score = models.CharField(
        max_length = 1,
        choices = SCORE_CHOICES,
        default = SCORE_A
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.score


class Student(models.Model):
    """Model representing a student."""
    name = models.CharField(
        max_length = 10,
        #primary_key = True,
        blank = False,
        help_text = "Enter your name"
    )

    student_id = models.CharField(
        max_length = 9,
        unique = True,
        null = False,
        blank = False,
        help_text = "Enter your student id"
    )

    """TEACHER_A = "2"
    SCORE_B = "3"
    SCORE_C = "4"
    SCORE_D = "5"
    SCORE_E = "6"
    SCORE_CHOICES = (
        (SCORE_A, "A: Perfect")
        (SCORE_B, "B: Good")
        (SCORE_C, "C: Normal")
        (SCORE_D, "D: Bad")
        (SCORE_E, "E: Lame")
    )"""
    teacher = models.CharField(
        max_length = 5,
        null = False,
        blank = False,
        help_text = "Enter your teacher name"
    )

    email = models.EmailField(
        blank = False,
        help_text = "Enter your email"
    )

    #preference = models.ForeignKey("Preference", on_delete = models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Form(models.Model):
    """Model representing a form."""
    name = models.CharField(
        max_length = 10,
        null = False,
        blank = False,
        help_text = "Enter form name"
    )

    form_url = models.URLField(
        null = False,
        blank = False,
        help_text = "Enter form url"
    )

    #student = models.OneToOneField("Student", on_delete = models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name