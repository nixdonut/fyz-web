import uuid
from django.db import models
from django.contrib.auth.models import User
 
SUBJECT_CHOICES = (
    ('Algebra', 'Algebra'),
    ('Combinatorics', 'Combinatorics'),
    ('Geometry', 'Geometry'),
    ('Number Theory', 'Number Theory'),
)
SOURCE_CHOICES = (
    ('Euclidean Geometry in Mathematical Olympiads by Evan Chen', 'Euclidean Geometry in Mathematical Olympiads by Evan Chen'),
    ('Modern Olympiad Number Theory by Aditya Khurmi', 'Modern Olympiad Number Theory by Aditya Khurmi'),
    ('Stephan Wagner\'s Combinatorics Handout', 'Stephan Wagner\'s Combinatorics Handout'),
    ('Olympiad Combinatorics by Pranav Sriram', 'Olympiad Combinatorics by Pranav Sriram'),
    ('Secrets in Inequalities (Volume 1) by Pham Kim Hung', 'Secrets in Inequalities (Volume 1) by Pham Kim Hung'),
    ('Secrets in Inequalities (Volume 2) by Pham Kim Hung', 'Secrets in Inequalities (Volume 2) by Pham Kim Hung'),
    ('Evan Chen\'s Functional Equations Handout', 'Evan Chen\'s Functional Equations Handout'),
)

class Unit(models.Model):

    SUBJECT_CHOICES = (
        ('Algebra', 'Algebra'),
        ('Combinatorics', 'Combinatorics'),
        ('Geometry', 'Geometry'),
        ('Number Theory', 'Number Theory'),
    )
    SOURCE_CHOICES = (
        ('Euclidean Geometry in Mathematical Olympiads by Evan Chen', 'Euclidean Geometry in Mathematical Olympiads by Evan Chen'),
        ('Modern Olympiad Number Theory by Aditya Khurmi', 'Modern Olympiad Number Theory by Aditya Khurmi'),
        ('Stephan Wagner\'s Combinatorics Handout', 'Stephan Wagner\'s Combinatorics Handout'),
        ('Olympiad Combinatorics by Pranav Sriram', 'Olympiad Combinatorics by Pranav Sriram'),
        ('Secrets in Inequalities (Volume 1) by Pham Kim Hung', 'Secrets in Inequalities (Volume 1) by Pham Kim Hung'),
        ('Secrets in Inequalities (Volume 2) by Pham Kim Hung', 'Secrets in Inequalities (Volume 2) by Pham Kim Hung'),
        ('Evan Chen\'s Functional Equations Handout', 'Evan Chen\'s Functional Equations Handout'),
    )
    idx = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 30, choices = SUBJECT_CHOICES)
    source = models.CharField(max_length = 200, choices = SOURCE_CHOICES)
    pdf = models.FileField(upload_to = "units/")
    solutions = models.FileField(null = True, blank = True, upload_to = "solutions/")
    user = models.ForeignKey(User, on_delete = models.CASCADE)