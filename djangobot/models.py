# -*- coding: utf-8 -*-
# vim:tabstop=4:shiftwidth=4:expandtab

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Tebelog(models.Model):
    title = models.CharField(max_length=190, primary_key=True,)
    body = models.TextField(blank=True, null=True,)
    url = models.TextField(blank=True, null=True,)
    image = models.ImageField(upload_to='images', blank=True, null=True,)
    score = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True,)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    CATEGORY_CHOICES = (
        (ita, _('Itarian')),
        (chn, _('Chinese')),
        (jpn, _('Japanese')),
        (oth, _('Other'))
    )
    category = models.CharField(
        max_length=190, default=ORDER_RELATED,
        choices=CATEGORY_CHOICES)
