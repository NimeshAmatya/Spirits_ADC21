from django.shortcuts import render
#from django.views.generic import ListView, DetailView
from .models import Add
from .forms import AddForm

# Create your views here.

'''
def home(request):
	context = {
	'posts': Post.objects.all()
	}
	return render(request, 'roomfinder/home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] #latest post comes at top

class PostDetailView(DetailView):
	model = Post


def about(request):
	return render(request, 'blog/about.html',{'title': 'About'})
'''

def add(request):
	form = AddForm()
	if request.method == "POST":
		form = AddForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('start:home')

	return render(request,"addpost/addpost.html",{"form":form})		


