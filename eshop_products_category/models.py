from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=120,verbose_name='title')
    name = models.CharField(max_length=120,verbose_name='title in Url')


    class Meta:
        verbose_name = 'title'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

