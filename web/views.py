from django.shortcuts import render

def index(request):
    template_name = "index.html"
    context = {}
    return render(request, template_name, context)


def servicios_web(request):
    template_name = "servicios/web.html"
    context = {}
    return render(request, template_name, context)


def servicios_iching(request):
    template_name = "servicios/iching.html"
    context = {}
    return render(request, template_name, context)