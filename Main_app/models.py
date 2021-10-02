from django.db import models

class user_info(models.Model):
    Username = models.CharField(blank=False, max_length=550)
    Pass = models.CharField(max_length=555, blank=False)

    def __str__(self):
        return self.Username

class contact_info(models.Model):
    Name = models.CharField(max_length=550, blank=False)
    Phone = models.IntegerField()
    B_phone = models.IntegerField()

    def __str__(self):
        return self.Name

# Create your models here.
