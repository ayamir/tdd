from django.conf.urls import include, url
from tddapp import views as list_views
from tdd import urls as list_urls

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
]
