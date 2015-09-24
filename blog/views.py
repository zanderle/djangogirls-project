from django.shortcuts import render


def index(request):
    context = {}  # insert data you want to show in the template
    return render(request, 'index.html', context)
