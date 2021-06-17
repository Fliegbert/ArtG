from django.urls import path
from . import views
from artg.views import (
    ArtistListView,
    ArtistDetailView,
    #PostCreateView,
    #ArtistUpdateView,
    #ArtistDeleteView
)

urlpatterns = [
    path('', views.home, name='artg-home'),
    path('about/', views.about, name='about'),
    path('resources/', views.rsc, name='rsc'),
    path('artist/', ArtistListView.as_view(), name='artist'),
    path('artist/<slug:slug>', ArtistDetailView.as_view(), name='artist-detail'),
    #path('artist/new/', ArtistCreateView.as_view(), name='artists-create'),
    #path('artist/<int:pk>/update/', ArtistUpdateView.as_view(), name='artists-update'),
    #path('artist/<int:pk>/delete/', ArtistDeleteView.as_view(), name='artists-delete'),
]