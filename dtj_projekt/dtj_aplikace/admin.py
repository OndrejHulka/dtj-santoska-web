from django.contrib import admin
from .models import Article, ArticleImage, Event, EventImage

# Admin pro články
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1
    max_num = 10  # maximálně 10 fotek

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('date_created',)
    date_hierarchy = 'date_created'
    inlines = [ArticleImageInline]

# Admin pro akce
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1
    max_num = 10  # maximálně 10 fotek

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('date_created',)
    date_hierarchy = 'date_created'
    inlines = [EventImageInline]