from django.db import models
import datetime


class Student(models.Model):
    objects = None
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True , blank=True)
    #    joined_date = models.DateField(null=True)
    #    FRESHMAN = "FR"
    #    SOPHOMORE = "SO"
    #    JUNIOR = "JR"
    #    SENIOR = "SR"
    #    GRADUATE = "GR"
    #    YEAR_IN_SCHOOL_CHOICES = [
    #        (FRESHMAN, "Freshman"),
    #        (SOPHOMORE, "Sophomore"),
    #        (JUNIOR, "Junior"),
    #        (SENIOR, "Senior"),
    #        (GRADUATE, "Graduate"),
    #    ]
    #    year_in_school = models.CharField(
    #        max_length=2,
    #        choices=YEAR_IN_SCHOOL_CHOICES,
    #        default=FRESHMAN,
    #    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    department = models.CharField(max_length=255, default='')
    COURSE_YEARS_CHOICES = (
        ('2', 'Two Years Course'),
        ('4', 'Four Years Course'),
    )
    no_of_course_years = models.CharField(max_length=10, choices=COURSE_YEARS_CHOICES, default='4')

    YEAR_CHOICES = [(r, r) for r in range(1959, datetime.date.today().year -7)]

    year_of_graduation = models.IntegerField(('Year Of Graduation'), choices=YEAR_CHOICES, default=datetime.datetime.now().year -8)
