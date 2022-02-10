from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Kurs, Frage, RichtigOderFalsch
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
	
class RichtigOderFalschHome(AuthListView): 
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_home.html'
	
class RichtigOderFalschCreate(AuthCreateView):
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_create.html'
    fields = '__all__'
    success_url = reverse_lazy('richtigoderfalsch_start')
	
class RichtigOderFalschDetail(AuthDetailView):
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_detail.html'

class RichtigOderFalschUpdate(AuthUpdateView):
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_update.html'
    fields = '__all__'
	
class RichtigOderFalschDelete(AuthDeleteView):
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_delete.html'
    success_url = reverse_lazy('richtigoderfalsch_start')

@login_required(login_url='/accounts/login/')
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_kurs = Kurs.objects.all().count()
    num_mcfrage = Frage.objects.all().count()
    num_rffrage = RichtigOderFalsch.objects.all().count()


    context = {
        'num_kurs': num_kurs,
        'num_mcfrage': num_mcfrage,
        'num_rffrage': num_rffrage
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
#    return render(request, 'mctest/mctest_select.html', context=context)


@login_required(login_url='/accounts/login/')	
def MCTestSelect(request):
  if request.method == "POST":
    form = TestSelectForm(request.POST)
    if form.is_valid():
       #form.save()
       #return HttpResponseRedirect('/index.html')
        data = form.cleaned_data.get("kurs")
        print(data.id)
        print(data.name)
        context = {
            'modulid':data.id,
            'modulname':data.name
        }
        return param_redirect(request, 'mctest_start', data.id) #, data.id, data.name)
	  
  else:
      form = TestSelectForm()
  return render(request, 'mctest/mctest_select.html', {'form': form})
  
@login_required(login_url='/accounts/login/')	
def RFTestSelect(request):
  if request.method == "POST":
    form = TestSelectForm(request.POST)
    if form.is_valid():
       #form.save()
       #return HttpResponseRedirect('/index.html')
        data = form.cleaned_data.get("kurs")
        print(data.id)
        print(data.name)
        context = {
            'modulid':data.id,
            'modulname':data.name
        }
        return param_redirect(request, 'rftest_start', data.id) #, data.id, data.name)
	  
  else:
      form = TestSelectForm()
  return render(request, 'rftest/rftest_select.html', {'form': form})

  
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
  return render(request, 'mctest/mctest_start.html', {'form': form})
  
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
  return render(request, 'mctest/para_test.html', {'form': form})

def str2bool(v):
  return v.lower() in ("on") 
 
@login_required(login_url='/accounts/login/')	  
def MCTestStart(request, arg1):
    if request.method == 'POST':
        print(request.POST)
        #fragen=Frage.objects.all()
        kurs=Kurs.objects.filter(id = arg1)
        print(kurs)
        fragen=Frage.objects.filter(kurs = arg1)
        fragenanzahl=len(fragen)
        punkte=0
        falsch=0
        korrekt=0
        total=0
        for f in fragen:
            total+=1
            answers=(request.POST.getlist(f.name))
            answercount=len(answers)
            boolantwort1=bool(False)
            boolantwort2=bool(False)
            boolantwort3=bool(False)
            boolantwort4=bool(False)

            if '1' in str(answers):
                boolantwort1=bool(True)
            if '2' in str(answers):
                boolantwort2=bool(True)
            if '3' in str(answers):
                boolantwort3=bool(True)
            if '4' in str(answers):
                boolantwort4=bool(True)
            print(boolantwort1)
            print(boolantwort2)
            print(boolantwort3)
            print(boolantwort4)

            print("Richige Antwort")
            print(f.antwort1richtig)
            print(f.antwort2richtig)
            print(f.antwort3richtig)
            print(f.antwort4richtig)
            print()

#

            if bool(boolantwort1) is bool(f.antwort1richtig) and bool(boolantwort2) is bool(f.antwort2richtig) and bool(boolantwort3) is bool(f.antwort3richtig) and bool(boolantwort4) is bool(f.antwort4richtig):
            #if bool(boolantwort1) == bool(f.antwort1richtig) and bool(boolantwort2) == bool(f.antwort2richtig) and bool(boolantwort3) == bool(f.antwort3richtig) and bool(boolantwort4) == bool(f.antwort4richtig):
            #if boolantwort1 == bool(f.antwort1richtig) and boolantwort2 == bool(f.antwort2richtig) and boolantwort3 == bool(f.antwort3richtig) and boolantwort4 == bool(f.antwort4richtig):
            #if bool(f.antwort1richtig) is boolantwort1 and bool(f.antwort2richtig) is boolantwort2 and bool(f.antwort3richtig) is boolantwort3 and bool(f.antwort4richtig) is boolantwort4:
            #if boolantwort1 == f.antwort1richtig and boolantwort2 == f.antwort2richtig and boolantwort3 == f.antwort3richtig and boolantwort4 == f.antwort4richtig:
                punkte+=10
                korrekt+=1
            else:
                falsch+=1

        punkte=korrekt*10
        prozent = punkte/(total*10) *100
        context = {
            'punkte':punkte,
            'fragenanzahl':fragenanzahl,
            'time': request.POST.get('timer'),
            'korrekt':korrekt,
            'falsch':falsch,
            'prozent':prozent,
            'total':total
        }
        return render(request,'mctest/mctest_result.html',context)
    else:
        #fragen=Frage.objects.all()
        kurs=Kurs.objects.filter(id = arg1)
        for k in kurs:
           kursname=k.name
           kursbeschreibung=k.beschreibung
        print(kursname)
        print(kursbeschreibung)
        fragen=Frage.objects.filter(kurs = arg1)
        context = {
            'fragen':fragen,
            'kursname':kursname,
			'kursbeschreibung':kursbeschreibung
        }
        return render(request,'mctest/mctest_start.html',context)
		
@login_required(login_url='/accounts/login/')	  
def RFTestStart(request, arg1):
    if request.method == 'POST':
        print(request.POST)
        #fragen=RichtigOderFalsch.objects.all()
        kurs=Kurs.objects.filter(id = arg1)
        print(kurs)
        rffragen=RichtigOderFalsch.objects.filter(kurs = arg1)
        rffragenanzahl=len(rffragen)
        punkte=0
        falsch=0
        korrekt=0
        total=0
        for rf in rffragen:
            total+=1
            #answers=(request.POST.getlist(rf.name))
            answers=request.POST.get(rf.name)
            boolantwort=bool(False)

            if '1' in str(answers):
                boolantwort=bool(True)
            if '2' in str(answers):
                boolantwort=bool(False)
            print(boolantwort)

            print("Richige Antwort")
            print(rf.behauptungrichtig)


#

            if bool(boolantwort) is bool(rf.behauptungrichtig):
                punkte+=10
                korrekt+=1
            else:
                falsch+=1

        punkte=korrekt*10
        prozent = punkte/(total*10) *100
        context = {
            'punkte':punkte,
            'fragenanzahl':rffragenanzahl,
            'time': request.POST.get('timer'),
            'korrekt':korrekt,
            'falsch':falsch,
            'prozent':prozent,
            'total':total
        }
        return render(request,'rftest/rftest_result.html',context)
    else:
        #fragen=RichtigOderFalsch.objects.all()
        kurs=Kurs.objects.filter(id = arg1)
        for k in kurs:
           kursname=k.name
           kursbeschreibung=k.beschreibung
        print(kursname)
        print(kursbeschreibung)
        rffragen=RichtigOderFalsch.objects.filter(kurs = arg1)
        context = {
            'rffragen':rffragen,
            'kursname':kursname,
			'kursbeschreibung':kursbeschreibung
        }
        return render(request,'rftest/rftest_start.html',context)