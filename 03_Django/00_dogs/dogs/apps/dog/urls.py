from django.conf.urls import url
import views

urlpatterns = [
    url(r'(?P<id>[\d]+)$', views.single_dog, name="single"),
    url(r'create$', views.create_dog, name="create"),
    # url(r'edit$', views.edit_dog, name="edit"),
    url(r'edit/second-time$', views.edit_second, name="edit2"),
    url(r'^(?P<id>[0-2]{,3})edit$', views.edit_dog, name="update"),
    url(r'(?P<id>[3-5]{2,4})/edit/second-time$', views.edit_second, name="update2"),
    url(r'(?P<id>[0-2]{3,})/destroy', views.delete_dog, name="delete"),
    url(r'^', views.index, name="index"),
]
