from django.db import models


class GuestEntry(models.Model):
    name = models.CharField(name='name', max_length=40, null=False, unique=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Hit(models.Model):
	pass
