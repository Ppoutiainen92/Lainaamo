from django.urls import path
from . import views
from .views import LibraryListView, LibraryDetailView

urlpatterns = [
    path('', LibraryListView.as_view(), name='library-list'),
    path('<int:pk>', LibraryDetailView.as_view(), name='library-detail')
]
