from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, Event, Plan, KontaktniZprava
from django.contrib import messages
from django.core.cache import cache

from .forms import KontaktniFormular

#pridat tri nejnovejsi clanky
def index(request):
    latest_articles = Article.objects.order_by('-date_created')[:3]
    
    context = {
        'latest_articles': latest_articles
    }
    
    return render(request, 'index.html', context)

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


class EventListView(ListView):
    model = Event
    template_name = 'probehleakce.html'
    context_object_name = 'events'
    paginate_by = 4  # 4 akce na stránku

class EventDetailView(DetailView):
    model = Event
    template_name = 'akce.html'
    context_object_name = 'event'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context

#staticke
def areal(request):
    return render(request, 'areal.html')

class PlanListView(ListView):
    model = Plan
    template_name = 'plan.html'
    context_object_name = 'plans'

#funkce ziskavani ip adress
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def kontakt(request):
    if request.method == 'POST':
        client_ip = get_client_ip(request)
        request_count = cache.get(f'form_requests:{client_ip}', 0)

        if request_count >= 5:
            messages.error(request, 'Příliš mnoho požadavků. Zkuste to prosím později.')
            return render(request, 'kontakt.html', {
                'form': KontaktniFormular(),
            })

        cache.set(f'form_requests:{client_ip}', request_count + 1, 60)
        
        form = KontaktniFormular(request.POST)
        if form.is_valid():
            zprava = form.save(commit=False)
            zprava.ip_adresa = client_ip
            zprava.save()

            messages.success(request, 'Vaše zpráva byla úspěšně odeslána!')
            form = KontaktniFormular()
        else:
            messages.error(request, 'Odeslání zprávy selhalo. Zkontrolujte formulář.')
    else:
        form = KontaktniFormular()  

    return render(request, 'kontakt.html', {  
        'form': form,
    })

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

def custom_403(request, exception):
    return render(request, '403.html', status=403)

def custom_400(request, exception):
    return render(request, '400.html', status=400)