from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from .models import Post
# Create your views here.


# def homePageView(request):
#     return HttpResponse("Hello World")

class HomePageView(TemplateView):
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class HomePageView(ListView):
    model=Post
    template_name="home.html"





