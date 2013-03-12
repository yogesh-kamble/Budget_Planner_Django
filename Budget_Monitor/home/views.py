from django.shortcuts import render_to_response, render
# Create your views here.

def home_page(request):
    '''
    render to home page
    '''
    return render_to_response("home.html")

