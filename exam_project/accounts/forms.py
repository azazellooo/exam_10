from django import forms

from accounts.models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'style': 'width: 300px;'})

    class Meta:
        model = Profile
        fields = ['phone_number']
