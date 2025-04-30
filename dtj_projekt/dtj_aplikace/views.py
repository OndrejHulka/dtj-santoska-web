from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article

#pridat tri nejnovejsi clanky
def index(request):
    return render(request, 'index.html')

#nic nemenit
def historie(request):
    return render(request, 'historie.html')

#pridat databazi
class ArticleListView(ListView):
    model = Article
    template_name = 'aktuality.html'
    context_object_name = 'articles'
    paginate_by = 4  # 4 články na stránku


#detailni clanek
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'clanek.html'
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context

#staticke
def areal(request):
    return render(request, 'areal.html')

#vytvorit databazi
def plan(request):
    return render(request, 'plan.html')

#vytvorit databazi
def probehle_akce(request):
    return render(request, 'probehleakce.html')

#vytvorit form
def kontakt(request):
    return render(request, 'kontakt.html')
