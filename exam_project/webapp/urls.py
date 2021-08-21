from django.urls import path

from webapp.views import ModeratedAdvertListView, UnModeratedAdvertListView

app_name = 'adverts'


urlpatterns = [
    path('', ModeratedAdvertListView.as_view(), name='moderated-list'),
    path('unmoderated/', UnModeratedAdvertListView.as_view(), name='unmoderated-list'),
]
