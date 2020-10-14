from django.urls import path
from . import views
from .views import LibraryListView

urlpatterns = [
    path('', LibraryListView.as_view(), name='index'),

]
