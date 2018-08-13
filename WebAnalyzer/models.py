# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from rest_framework import exceptions
from WebAnalyzer.tasks import analyzer_by_path
from WebAnalyzer.utils import filename
import ast


class ImageModel(models.Model):
    image = models.ImageField(upload_to=filename.uploaded_date)
    token = models.AutoField(primary_key=True)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(ImageModel, self).save(*args, **kwargs)
        task_get = ast.literal_eval(str(analyzer_by_path.delay(self.image.path).get()))
        for result in task_get:
            for item in result.items():
                self.result.create(layer=item[0], feature=item[1])
        super(ImageModel, self).save()


class ResultModel(models.Model):
    result_model = models.ForeignKey(ImageModel, related_name='result', on_delete=models.CASCADE)
    layer = models.TextField(null=True, unique=False)
    feature = models.TextField(null=True, unique=False)
    # feature = models.BinaryField(null=True, unique=False, editable=True)