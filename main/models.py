import uuid
from django.db import models
from django.contrib.auth.models import User
''''''
SOURCES_CHOICES = 0
with open('main/sources.txt') as f:
        choices = []
        for line in f:
            value = line.strip()
            choice = (value, value)
            choices.append(choice)
        SOURCES_CHOICES = tuple(choices)
SUBJECT_CHOICES = (
    ('Algebra', 'Algebra'),
    ('Geometry', 'Geometry'),
    ('Combinatorics', 'Combinatorics'),
    ('Number Theory', 'Number Theory'),
)

class Unit(models.Model):
    SUBJECT_CHOICES = (
    ('Algebra', 'Algebra'),
    ('Geometry', 'Geometry'),
    ('Combinatorics', 'Combinatorics'),
    ('Number Theory', 'Number Theory'),
)
   
    SOURCES_CHOICES = 0
    with open('main/sources.txt') as f:
        choices = []
        for line in f:
            value = line.strip()
            choice = (value, value)
            choices.append(choice)
        SOURCES_CHOICES = tuple(choices)
    
    idx = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 30, choices = SUBJECT_CHOICES)
    source = models.CharField(max_length = 200, choices = SOURCES_CHOICES)
    pdf = models.FileField(upload_to = "units/")
    solutions = models.FileField(null = True, blank = True, upload_to = "solutions/")
    user = models.ForeignKey(User, on_delete = models.CASCADE)

