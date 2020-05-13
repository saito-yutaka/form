from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=30)
    exp_total = models.IntegerField(verbose_name='経験値', default=10)

    def __str__(self):
        return f"{self.name}  {self.exp_total}"
