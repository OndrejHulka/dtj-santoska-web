from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulek")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    main_image = models.ImageField(upload_to='static/articles/main_images/', verbose_name="Titulní fotka")
    content = models.TextField(verbose_name="Obsah")
    date_created = models.DateField(auto_now_add=True, verbose_name="Datum vytvoření")
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Článek"
        verbose_name_plural = "Články"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='static/articles/additional_images/', verbose_name="Fotka")
    
    class Meta:
        verbose_name = "Fotka článku"
        verbose_name_plural = "Fotky článku"


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulek")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    main_image = models.ImageField(upload_to='static/events/main_images/', verbose_name="Titulní fotka")
    content = models.TextField(verbose_name="Obsah")
    date_created = models.DateField(auto_now_add=True, verbose_name="Datum vytvoření")
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Akce"
        verbose_name_plural = "Akce"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='static/events/additional_images/', verbose_name="Fotka")
    
    class Meta:
        verbose_name = "Fotka akce"
        verbose_name_plural = "Fotky akce"