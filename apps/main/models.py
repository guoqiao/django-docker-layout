from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Action(object):
    LIST = 'list'
    ADD = 'add'

    EDIT = 'edit'
    DELETE = 'delete'
    DETAIL = 'detail'


class GenericModel(models.Model):

    class Meta:
        abstract = True

    @classmethod
    def url_name(cls, action):
        return '%s_%s' % (cls.__name__, action)

    @classmethod
    def list_url(cls):
        url_name = cls.url_name(Action.LIST)
        return reverse(url_name)

    @classmethod
    def add_url(cls):
        url_name = cls.url_name(Action.ADD)
        return reverse(url_name)

    def edit_url(self):
        url_name = self.__class__.url_name(Action.EDIT)
        return reverse(url_name, kwargs={'pk': self.pk})

    def delete_url(self):
        url_name = self.__class__.url_name(Action.DELETE)
        return reverse(url_name, kwargs={'pk': self.pk})

    def detail_url(self):
        url_name = self.__class__.url_name(Action.DELETE)
        return reverse(url_name, kwargs={'pk': self.pk})


class Blog(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    user = models.ForeignKey(User)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    publish_at = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def is_draft(self):
        return not self.publish_at
