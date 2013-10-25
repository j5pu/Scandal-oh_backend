# -*- coding: utf-8 -*-
import os
import re

from django.contrib.auth.models import User, UserManager, Group
from django.db import models
from services.utils import delete_file
from settings.common import TEST_MODE

class CustomUser(User):
    class Meta:
        verbose_name = 'Custom user'
        verbose_name_plural = 'Custom users'

    objects = UserManager()

    def save(self, *args, **kwargs):
        if type(self) is CustomUser and not self.pk:
            self.set_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    def get_photo_path(self, filename):
        if self.pk:
            fileName, fileExtension = os.path.splitext(filename)
            path = 'photos/cat_%s/photo_%s%s' % (self.category.id, self.id, fileExtension)
            if TEST_MODE:
                return 'test/' + path
            return path
        else:
            return 'delete_me'

    user = models.ForeignKey(CustomUser, related_name='photos', blank=False)
    category = models.ForeignKey(Category, related_name='photos', blank=False, null=False)
    title = models.CharField(max_length=140, blank=False, null=False)
    img = models.FileField(upload_to=get_photo_path, null=True, blank=True)
    visits_count = models.PositiveIntegerField(default=0, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.pk) + '_' + self.title

    # def save(self, *args, **kwargs):
    #     """
    #     Cada vez que guardamos una foto lo hacemos en
    #     """
    #     super(Coupon, self).save(*args, **kwargs)
    #     if self.img:
    #         resize_img_width(self.img.path, 350)

    def delete(self, *args, **kwargs):
        if self.img:
            delete_file(self.img)
        super(Photo, self).delete(*args, **kwargs)

    def get_img_thumbnail_name(self):
        return re.sub(r'(?:_a)?\.([^.]*)$', r'.p.\1', self.img.name)

    def get_img_thumbnail_path(self):
        return re.sub(r'(?:_a)?\.([^.]*)$', r'.p.\1', self.img.path)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, related_name='comments', blank=False)
    photo = models.ForeignKey(Photo, related_name='comments', blank=False)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

