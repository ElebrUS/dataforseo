from django.db import models
from django.contrib.auth.models import User
from locations.models import Country, Location
from django.utils.timezone import now


class SearchEngine(models.Model):
    name = models.CharField(verbose_name='Search Engine Api Name', max_length=256)
    display_name = models.CharField(verbose_name='Search Engine Display Name', max_length=256)

    def __str__(self):
        return str(self.display_name)


class Order(models.Model):
    id_api = models.CharField(verbose_name='Id in Api', max_length=256, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, verbose_name='Country', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, verbose_name='Location', on_delete=models.SET_NULL, null=True)
    engine = models.ForeignKey(SearchEngine, verbose_name='Search Engine', on_delete=models.SET_NULL, null=True)
    keyword = models.CharField(verbose_name='Search keyword', max_length=256)
    start = models.DateTimeField(verbose_name='Date Add', default=now)
    end = models.DateTimeField(verbose_name='Date Done', null=True, blank=True, default=None)
    lang = models.CharField(verbose_name='Language Code', default='en', max_length=2)
    status = models.BooleanField(default=False, verbose_name='Status')

    def __str__(self):
        return '{} - "{}"'.format(self.user, self.keyword)


class DataOrder(models.Model):
    order = models.ForeignKey(Order, verbose_name='Order of element', on_delete=models.CASCADE)
    type = models.CharField(verbose_name='Type of element', max_length=256)
    rank_group = models.IntegerField(verbose_name='group rank in SERP')
    rank_absolute = models.IntegerField(verbose_name='absolute rank in SERP')
    domain = models.CharField(verbose_name='domain in SERP', max_length=256)
    title = models.CharField(verbose_name='title of the results element in SERP', max_length=256)
    description = models.TextField(verbose_name='description of the results element in SERP')
    url = models.CharField(verbose_name='relevant URL in SERP', max_length=256)
    breadcrumb = models.CharField(verbose_name='breadcrumb in SERP', max_length=256)

    def __str__(self):
        return '{} > {}'.format(self.order, self.title)
