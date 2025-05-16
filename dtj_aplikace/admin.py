from django.contrib import admin
from .models import Article, ArticleImage, Event, EventImage, Plan, KontaktniZprava

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

#admin pro Plan
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'start_time', 'end_time', 'location', 'has_pdf')
    list_filter = ('day',)
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'day'
    
    def has_pdf(self, obj):
        return bool(obj.pdf_file)
    has_pdf.boolean = True
    has_pdf.short_description = "PDF"

@admin.register(KontaktniZprava)
class KontaktniZpravaAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'email', 'cas_vytvoreni', 'ip_adresa')
    list_filter = ('cas_vytvoreni',)
    search_fields = ('jmeno', 'email', 'zprava')
    readonly_fields = ('cas_vytvoreni', 'ip_adresa')
    
    def has_change_permission(self, request, obj=None):
        # Zamezit úpravám zpráv (jen čtení)
        return False