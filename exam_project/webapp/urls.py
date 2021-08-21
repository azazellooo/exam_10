from django.urls import path

from webapp.views import (
    ModeratedAdvertListView,
    UnModeratedAdvertListView,
    AdvertDetailView,
    approve_ad,
    reject_ad,
    AdvertCreateView,
    AdvertUpdateView
)

app_name = 'adverts'


urlpatterns = [
    path('', ModeratedAdvertListView.as_view(), name='moderated-list'),
    path('unmoderated/', UnModeratedAdvertListView.as_view(), name='unmoderated-list'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='detail'),
    path('<int:pk>/update', AdvertUpdateView.as_view(), name='update'),
    path('create/', AdvertCreateView.as_view(), name='create'),
    path('int:pk/approve/', approve_ad, name='approve'),
    path('int:pk/reject/', reject_ad, name='reject'),
]
