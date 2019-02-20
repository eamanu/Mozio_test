from django.db import models


class Providers(models.Model):
    """This is the model of a Provider"""
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=255, null=False)
    language = models.CharField(max_length=255, null=False)
    currency = models.CharField(max_length=255, null=False)

    def __str__(self):
        """"Return a redeable representation of the model Providers"""
        return "%s - %s" % (self.name, self.email)
