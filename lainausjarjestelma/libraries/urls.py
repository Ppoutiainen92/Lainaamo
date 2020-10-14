from django.urls import path
from . import views
from .views import LibraryListView
from libraries import views as library_views

urlpatterns = [
    path('', LibraryListView.as_view(), name='library-list'),
    path('<int:pk>', library_views.library_detail_view, name='library-detail')
]
