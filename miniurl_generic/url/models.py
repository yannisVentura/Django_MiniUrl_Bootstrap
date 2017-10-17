from __future__ import unicode_literals

from django.db import models


class MiniUrl(models.Model):
    """
        Define an MiniUrl object.
        A url will be defined by a complete url, a code, a creation date, a pseudo and the number of acess to this url
    """
    url_complete = models.URLField(max_length=255, unique=True)
    code = models.IntegerField(unique=True, default=0)
    date_creation = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Date de parution')
    pseudo = models.CharField(max_length=10)
    nb_acces = models.IntegerField(default=0)

    def __str__(self):
        return str(self.url_complete)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('mini_url:create-miniurl')
