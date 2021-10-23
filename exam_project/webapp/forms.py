from django import forms

from webapp.models import Advert


class AdvertForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AdvertForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'style': 'width: 300px; margin-top: 0'})

    class Meta:
        model = Advert
        fields = ['title', 'description', 'category', 'picture', 'price']


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Search')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'search-input', 'placeholder': 'search'})
