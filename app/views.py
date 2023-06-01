from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a' : 20}
    d1={'a':200, 'b':30}
    d2={'a':1000, 'b':7000, 'c':8000, 'd':9000}
    return render(request, 'condition.html', context=d2)

def loop(request):
    d={'name':'Tushar'}
    return render(request, 'loop.html', context=d)