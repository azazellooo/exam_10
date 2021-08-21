from datetime import date
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AdvertForm, SearchForm
from webapp.models import Advert

today = date.today()


class ModeratedAdvertListView(ListView):
    model = Advert
    template_name = 'advert/main_list.html'
    context_object_name = 'adverts'
    ordering = '-published_at'

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_value = self.get_search_value()
        return super().get(request, **kwargs)

    def get_context_data(self):
        context = super().get_context_data()
        context['search_form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search_value': self.search_value})
        return context

    def get_queryset(self):
        queryset = super(ModeratedAdvertListView, self).get_queryset()
        queryset.filter(is_moderated=True, is_rejected=False).exclude(is_deleted=True)
        if self.search_value:
                queryset = queryset.filter(
                    Q(title__icontains=self.search_value) |
                    Q(description__icontains=self.search_value)
                )
        return queryset


class UnModeratedAdvertListView(PermissionRequiredMixin, ListView):
    model = Advert
    template_name = 'advert/unmoderated_list.html'
    context_object_name = 'adverts'
    ordering = 'created_at'
    permission_required = 'webapp.can_view_new_ads'

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_value = self.get_search_value()
        return super().get(request, **kwargs)

    def get_context_data(self):
        context = super().get_context_data()
        context['search_form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search_value': self.search_value})
        return context

    def get_queryset(self):
        queryset = super(UnModeratedAdvertListView, self).get_queryset()
        queryset.filter(is_moderated=False, is_rejected=False)
        if self.search_value:
                queryset = queryset.filter(
                    Q(title__icontains=self.search_value) |
                    Q(description__icontains=self.search_value)
                )
        return queryset


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'advert/detail.html'
    context_object_name = 'advert'

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if not request.user.has_perm('webapp.can_view_ads') and not object.is_moderated:
            return HttpResponse(request, 'you dont have permission', status=403)
        return super(AdvertDetailView, self).get(request, *args, **kwargs)


class AdvertUpdateView(PermissionRequiredMixin, UpdateView):
    model = Advert
    form_class = AdvertForm
    template_name = 'advert/update.html'
    permission_required = 'webapp.change_advert'

    def form_valid(self, form):
        advert = form.save(commit=False)
        advert.is_moderated = False
        advert.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('adverts:detail', kwargs={'pk': self.kwargs.get('pk')})

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()


class AdvertCreateView(LoginRequiredMixin, CreateView):
    form_class = AdvertForm
    model = Advert
    template_name = 'advert/create.html'
    success_url = reverse_lazy('adverts:moderated-list')

    def form_valid(self, form):
        advert = form.save(commit=False)
        advert.author = self.request.user
        advert.save()
        return redirect(self.success_url)


class AdvertDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_advert'
    model = Advert
    template_name = 'advert/delete.html'
    context_object_name = 'advert'
    success_url = reverse_lazy('adverts:moderated-list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

    def delete(self, request, *args, **kwargs):
        advert = self.get_object()
        advert.is_deleted = True
        advert.save()
        return redirect(self.success_url)


def approve_ad(request, *args, **kwargs):
    if request.is_ajax and request.method == "POST":
        ad = get_object_or_404(Advert, pk=list(dict(request.POST).keys())[0])
        ad.is_moderated = True
        ad.published_at = today
        ad.save()
        return JsonResponse({'message': 'ad is successfully moderated! :) '}, status=200)
    return JsonResponse({"error": ""}, status=400, safe=False)


def reject_ad(request, *args, **kwargs):
    if request.is_ajax and request.method == "POST":
        ad = get_object_or_404(Advert, pk=list(dict(request.POST).keys())[0])
        ad.is_rejected = True
        ad.save()
        return JsonResponse({'message': f'ad "{ad.title}" is rejected! '}, status=200)
    return JsonResponse({"error": ""}, status=400, safe=False)

    # Create your views here.
