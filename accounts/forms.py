from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True
    )

    first_name = forms.CharField(
        max_length=100,
        required=True
    )

    last_name = forms.CharField(
        max_length=100,
        required=True
    )

    phone = forms.CharField(
        max_length=15,
        required=True
    )

    area = forms.CharField(
        max_length=100,
        required=True
    )

    class Meta:

        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'area',
            'password1',
            'password2',
        ]

    def clean_email(self):

        email = self.cleaned_data['email']

        if User.objects.filter(
            email__iexact=email
        ).exists():

            raise forms.ValidationError(
                'This email is already registered.'
            )

        return email

    def clean_phone(self):

        phone = self.cleaned_data['phone']

        phone = phone.strip()

        if not phone.isdigit():

            raise forms.ValidationError(
                'Phone number must contain only digits.'
            )

        if len(phone) != 10:

            raise forms.ValidationError(
                'Enter a valid 10-digit phone number.'
            )

        return phone