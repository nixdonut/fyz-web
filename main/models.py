import uuid
from django.db import models
from django.contrib.auth.models import User
 
SUBJECT_CHOICES = (
    ('Algebra', 'Algebra'),
    ('Combinatorics', 'Combinatorics'),
    ('Geometry', 'Geometry'),
    ('Number Theory', 'Number Theory'),
)

class Unit(models.Model):

    SUBJECT_CHOICES = (
        ('Algebra', 'Algebra'),
        ('Combinatorics', 'Combinatorics'),
        ('Geometry', 'Geometry'),
        ('Number Theory', 'Number Theory'),
    )
    idx = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 30, choices = SUBJECT_CHOICES)
    source = models.CharField(max_length = 200)
    pdf = models.FileField(upload_to = "units/")
    solutions = models.FileField(null = True, blank = True, upload_to = "solutions/")
    user = models.ForeignKey(User, on_delete = models.CASCADE)