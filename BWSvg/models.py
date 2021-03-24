from django.db import models

class BeforeImage(models.Model):
    name = models.TextField(unique=True)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class AfterImage(models.Model):
    name = models.TextField(unique=True)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name