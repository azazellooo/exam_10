from django.views.generic import ListView

from webapp.models import Advert


class ModeratedAdvertListView(ListView):
    model = Advert
    template_name = 'advert/main_list.html'
    context_object_name = 'adverts'
    ordering = '-published_at'

    def get_queryset(self):
        queryset = super(ModeratedAdvertListView, self).get_queryset()
        return queryset.filter(is_moderated=True, is_rejected=False)


class UnModeratedAdvertListView(ListView):
    model = Advert
    template_name = 'advert/unmoderated_list.html'
    context_object_name = 'adverts'
    ordering = 'created_at'

    def get_queryset(self):
        queryset = super(UnModeratedAdvertListView, self).get_queryset()
        return queryset.filter(is_moderated=False, is_rejected=False)