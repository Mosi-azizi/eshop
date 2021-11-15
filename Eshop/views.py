from django.shortcuts import render
from eshop_slider.models import Slider

def header(requst,*args,**kwargs):
    context={

    }
    return render(requst, 'shared/Header.html', context)


def footer(requst, *args, **kwargs):
    context = {

    }
    return render(requst, 'shared/Footer.html', context)

def home_page(request):
    sliders = Slider.objects.all()
    context={
        'sliders':sliders
    }
    return render(request,'home_page.html',context)