from django.shortcuts import render
from django.views import generic
from . import models
class blogindex(generic.ListView):
	queryset = models.entry.objects.published()
	template_name = 'home.html'
	paginate_by = 2
class blogdetail(generic.DetailView):
	model = models.entry
	template_name = "post.html"
	


# Create your views here.
