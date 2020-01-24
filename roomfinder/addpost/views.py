from django.shortcuts import render, redirect
#from django.views.generic import ListView, DetailView
from .models import Add
from .forms import AddForm
from django.contrib import messages

# Create your views here.



def add(request):
	form = AddForm()
	if request.method == "POST":
		form = AddForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('start:home')

	messages.info(request, 'Your post has been uploaded.')
	return render(request,"addpost/addpost.html",{"form":form})	

def delete(request, pk):
	photo = Add.objects.get(pk = pk)
	photo.delete()
	return redirect('start:home')
		


