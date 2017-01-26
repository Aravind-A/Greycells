from django.conf.urls import url
from .views import q_view

urlpatterns = [
    url(r'^(?P<sluggy>\S+)$',q_view,name='q_view'),
    ]