from .forms import CommentForm
from django.views.generic.base import RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import artist, Comment


# Create your views here.

def home(request):
    return render(request, 'artg/home.html')

class ArtistListView(ListView):
    model = artist
    template_name = 'artg/artists.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'artists'

class ArtistDetailView(DetailView):
    model = artist
    slug_field = "slug"
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        
        if form.is_valid():
            artist = self.get_object()
            form.instance.user = request.user
            form.instance.artist = artist
            
            form.save()

            return redirect(reverse("artist-detail", kwargs={
                'slug': artist.slug
            }))
        
    def get_context_data(self, **kwargs):
        artist_comments_count = Comment.objects.all().filter(artist=self.object.id).count()
        artist_comments = Comment.objects.all().filter(artist=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'artist_comments': artist_comments,
            'artist_comments_count': artist_comments_count,
        })
        return context


    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['artist_list'] = artist.objects.all()
        #return context

#class ArtistUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    #model = artist
    #fields = ['artist', 'description']

    #def form_valid(self, form):
        #form.instance.author = self.request.user
        #return super().form_valid(form)

    #def test_func(self):
        #post = self.get_object()
        #if self.request.user == post.author:
            #return True
        #return False

#class ArtistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    #model = artist
    #success_url = 'artg-home'

    #def test_func(self):
        #post = self.get_object()
        #if self.request.user == post.author:
            #return True
        #return False

def rsc(request):
    return render(request, 'artg/rsc.html')

def about(request):
    return render(request, 'artg/about.html')