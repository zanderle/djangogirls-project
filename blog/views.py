from django.shortcuts import render

def home(request):
	context = {}  # insert data you want to show in the template
	return render(request, 'home.html', context)

def calculator_view(request):
	return render(request, 'calculator.html', {})
