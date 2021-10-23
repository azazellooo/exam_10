from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView, UpdateView
from django.views.generic.list import MultipleObjectMixin

from accounts.forms import ProfileForm
from accounts.models import Profile


class UserDetailView(DetailView, MultipleObjectMixin):
    model = get_user_model()
    template_name = 'profile.html'
    paginate_by = 5
    paginate_orphans = 1
    context_object_name = 'user_obj'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_object().advert.all()
        return super(UserDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        page_owner = self.get_object()
        if self.request.user != page_owner:
            context['adverts'] = page_owner.advert.filter(is_moderated=True)
            return context
        context['adverts'] = page_owner.advert.exclude(is_deleted=True)
        return context


class PhoneNumberUpdateView(PermissionRequiredMixin, UpdateView):
    model = Profile
    template_name = 'registration/update_profile.html'
    form_class = ProfileForm
    context_object_name = 'profile'
    permission_required = 'account.change_profile'

    def has_permission(self):
        return self.get_object().user == self.request.user or super().has_permission()

    def get_success_url(self):
        user_obj = User.objects.get(profile__id=self.kwargs.get('pk'))
        return reverse('accounts:profile', kwargs={'pk': user_obj.id})

# Create your views here.
