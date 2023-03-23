from django.urls import path, include, reverse_lazy
from hakatonapp import views
from stravauth.views import StravaAuth

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', StravaAuth.as_view(url=reverse_lazy("home")), kwargs={"approval_prompt": "force"}),
]