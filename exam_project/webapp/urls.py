from django.urls import path

from webapp.views import ModeratedAdvertListView, UnModeratedAdvertListView, AdvertDetailView, approve_ad

app_name = 'adverts'


urlpatterns = [
    path('', ModeratedAdvertListView.as_view(), name='moderated-list'),
    path('unmoderated/', UnModeratedAdvertListView.as_view(), name='unmoderated-list'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='detail'),
    path('int:pk/approve/', approve_ad, name='approve')
]
