from django import forms
from django.contrib.auth import authenticate
# from AdminApp.Project.Project_models import NrsProject
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Company


class Frm_login(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Frm_login, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.all()

    company = forms.ModelChoiceField(required=True, queryset=None, widget=forms.Select(attrs={'class': 'inputMaterial', 'required': 'true'}))
    username = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'inputMaterial', 'type': 'text', 'required': 'true'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'inputMaterial ', 'type': 'password', 'required': 'true', 'autocomplete': 'off'}))

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        user = authenticate(username=username, password=password)
        return user


class FormCompany(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormCompany, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.all()

    company = forms.ModelChoiceField(required=True, queryset=None, widget=forms.Select(attrs={'class': 'inputMaterial', 'required': 'true'}))

    class Meta:
        model = Company
        fields = '__all__'