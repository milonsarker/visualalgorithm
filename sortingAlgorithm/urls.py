from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.index, name='index'),
        #sortingAlgorithm/bubble sort
        url(r'^(?P<algoName>[a-z]+)/$',views.sortingAlgo,name='sortingAlgo'),
        ]
