from django.urls import path, include
from hakatonapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('oauth/', include('social_django.urls', namespace='social')),
]