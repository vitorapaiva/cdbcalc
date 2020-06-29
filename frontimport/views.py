from django.shortcuts import render

# Create your views here.
def import_form(request):
    return render(request, 'import_form.html')