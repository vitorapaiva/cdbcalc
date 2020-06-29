from django.shortcuts import render

# Create your views here.
def calc_form(request):
    return render(request, 'calc_form.html')