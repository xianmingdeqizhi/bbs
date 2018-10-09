# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    SEX = (
        ('M','男性'),
        ('F','女性'),
        ('U','保密'),
    )
    nickname = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=128)
    age = models.IntegerField(default=18)
    sex = models.CharField(max_length=8,choices=SEX)
    icon = models.ImageField()