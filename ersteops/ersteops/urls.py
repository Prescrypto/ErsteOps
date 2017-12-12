
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^emergency/', include('emergency.urls')),
    url(r'^notify/', include('notifications.urls')),
    url(r'^jet/', include('jet.urls','jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls','jet-dashboard')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
