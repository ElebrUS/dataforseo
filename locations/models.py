from django.db import models


# Create your models here.
class Country(models.Model):
    code = models.IntegerField(verbose_name='Country Code')
    name = models.CharField(verbose_name='Country Name', max_length=256)
    parent_code = models.IntegerField(verbose_name='Country Parent Code', blank=True, null=True)
    iso_code = models.CharField(verbose_name='Country ISO Code', max_length=5)
    type = models.CharField(verbose_name='Country Type', max_length=256)

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)


class Location(models.Model):
    country = models.ForeignKey(Country, verbose_name='Country', on_delete=models.CASCADE)
    code = models.IntegerField(verbose_name='Location Code')
    name = models.CharField(verbose_name='Location Name', max_length=256)
    parent_code = models.IntegerField(verbose_name='Location Parent Code', blank=True, null=True)
    type = models.CharField(verbose_name='Location Type', max_length=256)

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)
