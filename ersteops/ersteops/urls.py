
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from ajaxapi.views import get_subscriptor

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^emergency/', include('emergency.urls')),
    url(r'^notify/', include('notifications.urls')),
    url(r'^ajaxapi/getsubscriptor/',get_subscriptor, name="get_subscriptor"),
    # Jet Dashboard
    url(r'^jet/', include('jet.urls','jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls','jet-dashboard')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
