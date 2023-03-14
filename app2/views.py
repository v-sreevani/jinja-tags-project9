from django.shortcuts import render

# Create your views here.
def jinga_print(request):
    d={'name':'sree','age':6}
    return render(request,'jinja.html',context=d)