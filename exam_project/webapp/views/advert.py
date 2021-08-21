from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from webapp.models import Advert


class ModeratedAdvertListView(ListView):
    model = Advert
    template_name = 'advert/main_list.html'
    context_object_name = 'adverts'
    ordering = '-published_at'

    def get_queryset(self):
        queryset = super(ModeratedAdvertListView, self).get_queryset()
        return queryset.filter(is_moderated=True, is_rejected=False)


class UnModeratedAdvertListView(PermissionRequiredMixin, ListView):
    model = Advert
    template_name = 'advert/unmoderated_list.html'
    context_object_name = 'adverts'
    ordering = 'created_at'
    permission_required = 'webapp.can_view_new_ads'

    def get_queryset(self):
        queryset = super(UnModeratedAdvertListView, self).get_queryset()
        return queryset.filter(is_moderated=False, is_rejected=False)


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'advert/detail.html'
    context_object_name = 'advert'

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if not request.user.has_perm('webapp.can_view_ads') and not object.is_moderated:
            return HttpResponse(request, 'you dont have permission', status=403)
        return super(AdvertDetailView, self).get(request, *args, **kwargs)