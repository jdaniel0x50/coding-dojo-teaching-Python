from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<name>[\w]{3})$', views.single_person, name="single_person"),
    url(r'^', views.index, name="index"),
]
