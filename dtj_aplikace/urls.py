from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('historie/', views.historie, name='historie'),
    path('aktuality/', views.ArticleListView.as_view(), name='article_list'),
    path('clanek/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('probehleakce/', views.EventListView.as_view(), name='event_list'),
    path('akce/<slug:slug>/', views.EventDetailView.as_view(), name='event_detail'),
    path('areal/', views.areal, name='areal'),
    path('plan/', views.PlanListView.as_view(), name='plan'),
    path('kontakt/', views.kontakt, name='kontakt'),
]