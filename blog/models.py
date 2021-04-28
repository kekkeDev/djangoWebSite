from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from django.contrib.sites.models import Site
from django.conf import settings
import markdown
from bs4 import BeautifulSoup

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=255)
    content = MDTextField()
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='post_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def getToc(self):
        tocAll = markdown.markdown(self.content, extensions=['toc'])
        soup = BeautifulSoup(tocAll, "html.parser")
        return soup.select_one('.toc')

class ContentImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    content_image = models.ImageField(upload_to='editor/')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

class Reply(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

class SiteDetail(models.Model):
    site = models.OneToOneField(Site, verbose_name='Site', on_delete=models.PROTECT)
    title = models.CharField('sites title', max_length=255, default='title')
    description = models.TextField('sites description', max_length=255, default='description')
    keywords = models.CharField('sites keyword', max_length=255, default='keywords')
    author = models.CharField('author', max_length=255, default='author')
    email = models.EmailField('author E-mail address', max_length=255, default='your_mail@gmail.com')
    github = models.CharField('github account', max_length=255, blank=True)
    twitter = models.CharField('twitter account', max_length=255, blank=True)
    facebook = models.CharField('faceBook account', max_length=255, blank=True)
    instagram = models.CharField('instagram account', max_length=255, blank=True)
    linkedin = models.CharField('linkedin account', max_length=255, blank=True)
    google_ad_html = models.TextField('adSense HTML', blank=True)
    google_analytics_html = models.TextField('GA HTML', blank=True)

    def __str__(self):
        return self.author


def create_default_site_detail(sender, **kwargs):
    site = Site.objects.get(pk=settings.SITE_ID)
    SiteDetail.objects.get_or_create(site=site)