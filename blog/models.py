from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.
class Post (models.Model):

    #filtriranje da se vidi samo publish ne i draft
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')


    # opcijee za dropdown menu
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    #sta sve post treba da ima
    title = models.CharField(max_length=250)
    excerpt = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')

    objects = models.Manager() #default manager
    newManager = NewManager() #new manager


    #da svaki naslov pocetni bude link
    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])


    #kako da bude redosled
    class Meta:
        ordering = ('-publish', )


    #da title bude naslov u admin
    def __str__(self):
        return self.title