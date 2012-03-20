from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Category(MPTTModel):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')
    def __unicode__(self):
        return self.title
    class MPTTMeta:
        order_insertion_by = ['title']

class Algorithm(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    def __unicode__(self):
        return self.title

class AlgorithmImplementation(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    implements = models.ForeignKey(Algorithm)
    LANGUAGE_CHOICES = (
        ('python2', 'Python 2.x'),
        ('python3', 'Python 3.x'),
        ('c', 'C'),
        ('c++', 'C++'),
        ('java', 'Java'),
        ('c#', 'C#')
    )
    language = models.CharField(max_length=32, choices=LANGUAGE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    def __unicode__(self):
        return self.implements.title + " in " + self.language

class DataStructure(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    def __unicode__(self):
        return self.title

class DataStructureImplementation(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    implements = models.ForeignKey(DataStructure)
    LANGUAGE_CHOICES = (
        ('python2', 'Python 2.x'),
        ('python3', 'Python 3.x'),
        ('c', 'C'),
        ('c++', 'C++'),
        ('java', 'Java'),
        ('c#', 'C#')
        )
    language = models.CharField(max_length=32, choices=LANGUAGE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    def __unicode__(self):
        return self.implements.title + " in " + self.language

class Demonstration(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    def __unicode__(self):
        return self.title

class DemonstrationImplementation(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    implements = models.ForeignKey(Demonstration)
    LANGUAGE_CHOICES = (
        ('python2', 'Python 2.x'),
        ('python3', 'Python 3.x'),
        ('c', 'C'),
        ('c++', 'C++'),
        ('java', 'Java'),
        ('c#', 'C#')
        )
    language = models.CharField(max_length=32, choices=LANGUAGE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    def __unicode__(self):
        return self.implements.title + " in " + self.language

class TestSuite(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    TEST_TYPE_CHOICES = (
        ('a', 'Algorithm Test Suite'),
        ('s', 'Data Structure Test Suite')
        )
    test_type = models.CharField(max_length=1, choices=TEST_TYPE_CHOICES)
    algorithm_test = models.ForeignKey(Algorithm, blank=True, null=True)
    data_structure_test = models.ForeignKey(DataStructure, blank=True, null=True)
    def __unicode__(self):
        return self.title


class TestSuiteImplementation(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    implements = models.ForeignKey(TestSuite)
    LANGUAGE_CHOICES = (
        ('python2', 'Python 2.x'),
        ('python3', 'Python 3.x'),
        ('c', 'C'),
        ('c++', 'C++'),
        ('java', 'Java'),
        ('c#', 'C#')
        )
    language = models.CharField(max_length=32, choices=LANGUAGE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    def __unicode__(self):
        return self.implements.title + " in " + self.language

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    def __unicode__(self):
        return unicode(self.user)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User, dispatch_uid="users-profilecreation-signal")