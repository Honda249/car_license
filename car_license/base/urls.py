from django.urls import path        
from base.views import indexView

urlpatterns = [
    path('home/', indexView.HomePageView.as_view(),name='index')
]
