from django.db import models


class UrlModel(models.Model):
    """
    slug field store the unique Slug for an URL; used for identification
    url contains original URL
    """
    slug = models.SlugField(unique=True)
    url = models.TextField(null=False)
    short_url = models.TextField(null=True)

    def __str__(self):
        return sel.slug