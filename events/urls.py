from django.conf.urls import url
from events import views


urlpatterns = [
    url(r'$', views.EventListCreate.as_view(), name='event-list-create'),
]
