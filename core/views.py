from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def index_View(request):
    return render(request, "core/index.html", {})
def elements_View(request):
    return render(request, "core/elements.html", {})
def multimedia_View(request):
    return render(request, "core/multimedia.html", {})
def page_View(request):
    return render(request, "core/page.html", {})
def page1_View(request):
    return render(request, "core/page1.html", {})
def page2_View(request):
    return render(request, "core/page2.html", {})
def page3_View(request):
    return render(request, "core/page3.html", {})
