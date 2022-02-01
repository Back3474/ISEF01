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
from .forms import TestSelectForm
from .forms import ParaTestForm

from urlparams.redirect import param_redirect #???
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
#from django.urls import reverse
#from django.shortcuts import redirect

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

#@login_required(login_url='/accounts/login/')
#def test_select(request):
#
#    kurs_select = Kurs.objects.all()
#
#
#    context = {
#        'kurs_select': kurs_select,
#    }
#
#    return render(request, 'test/test_select.html', context=context)


@login_required(login_url='/accounts/login/')	
def TestSelect(request):
  if request.method == "POST":
    form = TestSelectForm(request.POST)
    if form.is_valid():
       #form.save()
       #return HttpResponseRedirect('/index.html')
        data = form.cleaned_data.get("kurs")
        print(data.id)
        print(data.name)
        return param_redirect(request, 'test_start', data.id) #, data.id, data.name)
	  
  else:
      form = TestSelectForm()
  return render(request, 'test/test_select.html', {'form': form})
  
@login_required(login_url='/accounts/login/')	
def TestStart(request, arg1): #, arg2
  if request.method == "POST":
    form = ParaTestForm(request.POST)
    if form.is_valid():
       #form.save()
       #return HttpResponseRedirect('/index.html')
        data1 = form.cleaned_data.get("arg1")
        #data2 = form.cleaned_data.get("arg2")
        #return param_redirect(request, 'index') #, data.id, data.name)
	  
  else:
      form = ParaTestForm()
      print(arg1)
      #print(arg2)
      form.fields["arg1"].initial = arg1
      #form.fields["arg2"].initial = arg2
  return render(request, 'test/test_start.html', {'form': form})
  
@login_required(login_url='/accounts/login/')	
def ParaTest(request, arg1): #, arg2
  if request.method == "POST":
    form = ParaTestForm(request.POST)
    if form.is_valid():
       #form.save()
       #return HttpResponseRedirect('/index.html')
        data1 = form.cleaned_data.get("arg1")
        #data2 = form.cleaned_data.get("arg2")
        #return param_redirect(request, 'index') #, data.id, data.name)
	  
  else:
      form = ParaTestForm()
      print(arg1)
      #print(arg2)
      form.fields["arg1"].initial = arg1
      #form.fields["arg2"].initial = arg2
  return render(request, 'test/para_test.html', {'form': form})

@login_required(login_url='/accounts/login/')	  
def TestStart2(request, arg1):
    if request.method == 'POST':
        print(request.POST)
        #fragen=Frage.objects.all()
        fragen=Frage.objects.filter(kurs = arg1)
        score=0
        wrong=0
        correct=0
        total=0
        for f in fragen:
            total+=1
            print(request.POST.get(f.name))
            print(f.antwort1)
            print()
            if f.name ==  request.POST.get(f.name):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'test/result.html',context)
    else:
        #fragen=Frage.objects.all()
        fragen=Frage.objects.filter(kurs = arg1)
        context = {
            'fragen':fragen
        }
        return render(request,'test/test_start.html',context)