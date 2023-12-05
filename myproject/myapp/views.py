from django.shortcuts import render

# Create your views here.
def Myform(request):
    return render(request,'app/form.html')