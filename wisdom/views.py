from django.shortcuts import render

# Create your views here.
def wisdom(request):
    return render(request, 'wisdom.html')
