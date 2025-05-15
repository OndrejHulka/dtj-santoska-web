from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
import datetime
from django.core.validators import FileExtensionValidator

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulek")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    main_image = models.ImageField(upload_to='static/articles/main_images/', verbose_name="Titulní fotka")
    content = models.TextField(verbose_name="Obsah")
    date_created = models.DateField(default=datetime.date.today, verbose_name="Datum vytvoření")
    
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
    date_created = models.DateField(default=datetime.date.today, verbose_name="Datum vytvoření")
    
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

class Plan(models.Model):
    title = models.CharField(max_length=255, verbose_name="Název události")
    description = models.TextField(verbose_name="Popis události", blank=True)
    day = models.DateField(verbose_name="Den")
    start_time = models.TimeField(verbose_name="Čas začátku")
    end_time = models.TimeField(verbose_name="Čas konce")
    location = models.CharField(max_length=255, verbose_name="Lokace")
    pdf_file = models.FileField(
        upload_to='static/plans/pdfs/', 
        verbose_name="PDF soubor", 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(['pdf'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        day_name = self.day.strftime("%A").lower()  # Get day name in lowercase
        return f"{self.title} - {day_name} {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"
    
    class Meta:
        verbose_name = "Plán"
        verbose_name_plural = "Plán"
        ordering = ['day', 'start_time']

class KontaktniZprava(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name='Jméno')
    email = models.EmailField(verbose_name='Email')
    zprava = models.TextField(verbose_name='Zpráva')
    cas_vytvoreni = models.DateTimeField(default=timezone.now, verbose_name='Čas vytvoření')
    ip_adresa = models.GenericIPAddressField(blank=True, null=True, verbose_name='IP adresa')
    
    class Meta:
        verbose_name = 'Kontaktní zpráva'
        verbose_name_plural = 'Kontaktní zprávy'
    
    def __str__(self):
        return f"Zpráva od {self.jmeno} ({self.email}) - {self.cas_vytvoreni.strftime('%d.%m.%Y %H:%M')}"