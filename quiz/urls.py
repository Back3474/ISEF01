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
from .views import index
from .views import TestSelect
from .views import ParaTest

urlpatterns = [
     #path('', KursHome.as_view(), name='kurs_start'),
	 path('', index, name='index'),
     path('kurs', KursHome.as_view(), name='kurs_start'),
	 path('frage', FrageHome.as_view(), name='frage_start'),
	 path('test', TestSelect, name='test_select'),
	 path('paratest', ParaTest, name='para_test'),
	 path('paratest/<arg1>-<arg2>', ParaTest, name='para_test'),
	 path('paratest/<arg1>', ParaTest, name='para_test'),
	 path('kurs/neu/', KursCreate.as_view(), name='neuer_kurs'),
	 path('frage/neu/', FrageCreate.as_view(), name='neue_frage'),
	 path('kurs/<int:pk>/', KursDetail.as_view(), name='kurs_detail'),
	 path('frage/<int:pk>/', FrageDetail.as_view(), name='frage_detail'),
	 path('kurs/<int:pk>/update/', KursUpdate.as_view(), name='kurs_update'),
	 path('frage/<int:pk>/update/', FrageUpdate.as_view(), name='frage_update'),
	 path('kurs/<int:pk>/delete/', KursDelete.as_view(), name='kurs_delete'),
	 path('frage/<int:pk>/delete/', FrageDelete.as_view(), name='frage_delete'),
]