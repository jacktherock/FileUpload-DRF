from django.conf.urls import url
from .views import FileView, delete
from django.urls import path

urlpatterns = [
    path('upload/', FileView.as_view(), name="file-upload"), # localhost:8000/file/upload/ -POST
    
    url(r'^delete/(?P<pk>[0-9]+)$', delete),

    #localhost:8000/file/delete/:id -DELETE
]