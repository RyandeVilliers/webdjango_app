from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# render function renders templates
def index(request):
    return render(request, 'pages/index.html')
    # render function takes request and location of index template

def about(request):
    return render(request, 'pages/about.html')
    # render function takes request and location of about template


