from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_api/', include('registration.urls')),
    path('index/', include('events.urls'))
]
