from django.conf.urls import url, include
from .views import user_profile_view


urlpatterns = [
    # url(r'^(?P<id>\d+)/$', user_profile_view, name='user_profile'),
    url('myProfile/', user_profile_view, name='user_profile'),

]