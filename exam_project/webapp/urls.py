from django.urls import path

from webapp.views import ModeratedAdvertListView

app_name = 'adverts'


urlpatterns = [
    path('', ModeratedAdvertListView.as_view(), name='moderated-list')
]
