from django.shortcuts import render

# Create your views here.

def add(request):
	form = AddForm()
	if request.method == "POST":
		form = AddForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('start:home')

	return render(request,"addpost/addpost.html",{"form":form})	

def roomlist(request):
	add = Add.objects.all()

	query = ""
	if request.GET:
		query  = request.GET['q']

		add = get_data_queryset(str(query))

	return render(request, "addpost/roomlist.html", {"adds":add})  

def delete(request, pk):
	photo = Add.objects.get(pk = pk)
	photo.delete()
	return redirect('start:home')
		

