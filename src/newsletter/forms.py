from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        #exclude = ['full_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extention = provider.split(".")
        # if not domain == "gmail":
        #     raise forms.ValidationError('this is not gmail')
        if not extention == "edu":
            raise forms.ValidationError('pls use a valid college email')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
