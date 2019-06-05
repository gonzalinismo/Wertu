from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import SuscripcionForm
# Create your views here.

def index(request):
	form = SuscripcionForm()
	context = {'form':form}
	return render(request,"index.html",context)

def suscrpicion():
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = SuscripcionForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
		# process the data in form.cleaned_data as required
		# ...
		# redirect to a new URL:
			return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
	else:
		form = SuscripcionForm()

	return render(request, 'index.html', {'form': form})