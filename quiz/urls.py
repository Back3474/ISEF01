from django.urls import path
from .views import KursHome
from .views import KursCreate
from .views import KursDetail
from .views import KursUpdate
from .views import KursDelete

from .views import FrageHome
from .views import FrageCreate
from .views import FrageDetail
from .views import FrageUpdate
from .views import FrageDelete
from .views import RichtigOderFalschHome
from .views import RichtigOderFalschCreate
from .views import RichtigOderFalschDetail
from .views import RichtigOderFalschUpdate
from .views import RichtigOderFalschDelete
from .views import ErgebnisHome
from .views import ErgebnisDetail
from .views import index
from .views import MCTestSelect
from .views import RFTestSelect
from .views import TestStart
from .views import MCTestStart
from .views import RFTestStart
from .views import ParaTest

urlpatterns = [
     #path('', KursHome.as_view(), name='kurs_start'),
	 path('', index, name='index'),
     path('kurs', KursHome.as_view(), name='kurs_start'),
	 path('frage', FrageHome.as_view(), name='frage_start'),
     path('richtigoderfalsch', RichtigOderFalschHome.as_view(), name='richtigoderfalsch_start'),
     path('ergebnis', ErgebnisHome.as_view(), name='ergebnis_start'),   	 
	 path('mctest', MCTestSelect, name='mctest_select'),
     path('rftest', RFTestSelect, name='rftest_select'),
	 path('mctest/<arg1>', MCTestStart, name='mctest_start'),
	 path('mctest/<arg1>/<arg2>', MCTestStart, name='mctest_start'),
     path('rftest/<arg1>', RFTestStart, name='rftest_start'),
     path('rftest/<arg1>/<arg2>', RFTestStart, name='rftest_start'),
	 path('paratest', ParaTest, name='para_test'),
	 path('paratest/<arg1>-<arg2>', ParaTest, name='para_test'),
	 path('paratest/<arg1>', ParaTest, name='para_test'),
	 path('kurs/neu/', KursCreate.as_view(), name='neuer_kurs'),
	 path('frage/neu/', FrageCreate.as_view(), name='neue_frage'),
     path('richtigoderfalsch/neu/', RichtigOderFalschCreate.as_view(), name='richtigoderfalsch_neue_frage'),
	 path('kurs/<int:pk>/', KursDetail.as_view(), name='kurs_detail'),
	 path('frage/<int:pk>/', FrageDetail.as_view(), name='frage_detail'),
     path('richtigoderfalsch/<int:pk>/', RichtigOderFalschDetail.as_view(), name='richtigoderfalsch_detail'),
     path('ergebnis/<int:pk>/', ErgebnisDetail.as_view(), name='ergebnis_detail'),
	 path('kurs/<int:pk>/update/', KursUpdate.as_view(), name='kurs_update'),
	 path('frage/<int:pk>/update/', FrageUpdate.as_view(), name='frage_update'),
     path('richtigoderfalsch/<int:pk>/update/', RichtigOderFalschUpdate.as_view(), name='richtigoderfalsch_update'),
	 path('kurs/<int:pk>/delete/', KursDelete.as_view(), name='kurs_delete'),
	 path('frage/<int:pk>/delete/', FrageDelete.as_view(), name='frage_delete'),
     path('richtigoderfalsch/<int:pk>/delete/', RichtigOderFalschDelete.as_view(), name='richtigoderfalsch_delete'),
]