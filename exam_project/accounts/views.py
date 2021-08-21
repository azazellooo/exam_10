from django.contrib.auth import get_user_model
from django.views.generic import DetailView


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        page_owner = self.get_object()
        if self.request.user != page_owner:
            context['adverts'] = page_owner.advert.filter(is_moderated=True)
            return context
        context['adverts'] = page_owner.advert.all()
        return context

# Create your views here.
