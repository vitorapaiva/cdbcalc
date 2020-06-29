from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/calc/', include('calc.urls')),
    path('api/v1/cdi/', include('importcdi.urls')),
    path('', include('frontcalc.urls')),
    path('import/', include('frontimport.urls')),
    path('admin/', admin.site.urls),
]