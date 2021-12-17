from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Kurs, Frage

# Create your views here.

class AuthListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class AuthDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class AuthCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
	
class AuthUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class AuthDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class KursHome(AuthListView): 
    model = Kurs
    template_name = 'kurs/kurs_home.html'

class KursCreate(AuthCreateView):
    model = Kurs
    template_name = 'kurs/kurs_create.html'
    fields = '__all__'
    success_url = reverse_lazy('kurs_start')
	
class KursDetail(AuthDetailView):
    model = Kurs
    template_name = 'kurs/kurs_detail.html'

class KursUpdate(AuthUpdateView):
    model = Kurs
    template_name = 'kurs/kurs_update.html'
    fields = '__all__'
	
class KursDelete(AuthDeleteView):
    model = Kurs
    template_name = 'kurs/kurs_delete.html'
    success_url = reverse_lazy('kurs_start')
	
class FrageHome(AuthListView): 
    model = Frage
    template_name = 'frage/frage_home.html'
	
class FrageCreate(AuthCreateView):
    model = Frage
    template_name = 'frage/frage_create.html'
    fields = '__all__'
    success_url = reverse_lazy('frage_start')
	
class FrageDetail(AuthDetailView):
    model = Frage
    template_name = 'frage/frage_detail.html'

class FrageUpdate(AuthUpdateView):
    model = Frage
    template_name = 'frage/frage_update.html'
    fields = '__all__'
	
class FrageDelete(AuthDeleteView):
    model = Frage
    template_name = 'frage/frage_delete.html'
    success_url = reverse_lazy('frage_start')

@login_required(login_url='/accounts/login/')
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_frage = Frage.objects.all().count()
    num_kurs = Kurs.objects.all().count()


    context = {
        'num_frage': num_frage,
        'num_kurs': num_kurs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)