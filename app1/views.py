from django.shortcuts import render

# Create your views here.


def calling(request):
    return render(request, 'calling.html')