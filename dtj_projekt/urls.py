from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dtj_aplikace.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'dtj_aplikace.views.custom_404'
handler500 = 'dtj_aplikace.views.custom_500'
handler403 = 'dtj_aplikace.views.custom_403'
handler400 = 'dtj_aplikace.views.custom_400'