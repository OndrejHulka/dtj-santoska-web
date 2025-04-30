from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('historie/', views.historie, name='historie'),
    path('aktuality/', views.ArticleListView.as_view(), name='article_list'),
    path('clanek/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('areal/', views.areal, name='areal'),
    path('plan/', views.plan, name='plan'),
    path('probehleakce/', views.probehle_akce, name='probehle_akce'),
    path('kontakt/', views.kontakt, name='kontakt'),
]