from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    code = models.CharField(max_length=50, null=True, blank=True)
    logo= models.FileField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
