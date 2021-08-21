from django.views.generic import ListView

from webapp.models import Advert


class ModeratedAdvertListView(ListView):
    model = Advert
    template_name = 'advert/main_list.html'
    context_object_name = 'adverts'
    ordering = '-published_at'

    def get_queryset(self):
        queryset = super(ModeratedAdvertListView, self).get_queryset()
        print(queryset.filter(is_moderated=True, is_rejected=False))
        return queryset.filter(is_moderated=True, is_rejected=False)
