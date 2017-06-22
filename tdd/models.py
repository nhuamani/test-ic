from django.db import models

# Create your models here.


class Animal(models.Model):

    name = models.CharField(max_length=20)
    sound = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name

    def speak(self):
        return 'The %s says "%s"' % (self.name, self.sound)
