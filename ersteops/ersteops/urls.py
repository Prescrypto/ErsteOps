
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from ajaxapi.views import get_subscriptor,get_symptom_zero, get_emergency_grade, get_tree_zero, get_full_tree

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^emergency/', include('emergency.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^units/', include('unit.urls')),
    url(r'^notify/', include('notifications.urls')),
    # Ajax Calls
    url(r'^ajaxapi/getsubscriptor/',get_subscriptor, name="get_subscriptor"),
    url(r'^ajaxapi/get_symptom/',get_symptom_zero, name="get_symptom"),
    url(r'^ajaxapi/get_emergency_grade/',get_emergency_grade, name="get_emergency_grade"),
    url(r'^ajaxapi/get_tree_zero/',get_tree_zero, name="get_tree_zero"),
    url(r'^ajaxapi/get_full_tree/',get_full_tree, name="get_full_tree"),

    # Decision tree
    url(r'^decisiontree/',include('decisiontree.urls')),
    # Jet Dashboard
    url(r'^jet/', include('jet.urls','jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls','jet-dashboard')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
