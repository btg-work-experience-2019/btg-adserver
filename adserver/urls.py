from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('display_ad_manager.urls')),
    path('placements/', include('display_ad_manager.urls')),
]
