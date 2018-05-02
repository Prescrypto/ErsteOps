
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from ajaxapi.views import get_subscriptor,get_symptom_zero

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^emergency/', include('emergency.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^units/', include('unit.urls')),
    url(r'^notify/', include('notifications.urls')),
    url(r'^ajaxapi/getsubscriptor/',get_subscriptor, name="get_subscriptor"),
    url(r'^ajaxapi/get_symptom/',get_symptom_zero, name="get_symptom"),
    url(r'^decisiontree/',include('decisiontree.urls')),
    # Jet Dashboard
    url(r'^jet/', include('jet.urls','jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls','jet-dashboard')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
