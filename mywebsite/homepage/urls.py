from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus/', views.aboutus, name ='about'),
    path('contactus/', views.contactus, name ='contact'),
    path('courses/', views.courses, name = 'courses'),
]
