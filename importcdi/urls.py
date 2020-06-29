from django.urls import path
from importcdi.views import import_cdi
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('import/', csrf_exempt(import_cdi), name='api_import_cdi'),
]