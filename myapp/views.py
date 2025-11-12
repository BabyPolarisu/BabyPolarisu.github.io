from django.shortcuts import render


# Create your views here.
def home(request):
	"""Render a minimal homepage."""
	context = {
		'title': 'Homepage',
		'message': 'Welcome to the simple Django + uvicorn homepage.'
	}
	return render(request, 'myapp/home.html', context)
