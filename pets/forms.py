from django import forms
from .models import Pet


class PetForm(forms.ModelForm):

    class Meta:

        model = Pet

        fields = [
            'name',
            'pet_type',
            'breed',
            'date_of_birth',
            'gender',
            'color',
            'identification_details',
            'photo',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name'
                }
            ),

            'pet_type': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'breed': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter breed'
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'gender': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'color': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter color'
                }
            ),

            'identification_details': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder':
                        'Example: White mark on chest, '
                        'blue collar, special identification...'
                }
            ),

            'photo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'image/jpeg,image/png,image/webp'
                }
            ),
        }

    def clean_name(self):

        name = self.cleaned_data['name'].strip()

        if len(name) < 2:

            raise forms.ValidationError(
                'Pet name must contain at least 2 characters.'
            )

        return name

    def clean_color(self):

        color = self.cleaned_data['color'].strip()

        if len(color) < 2:

            raise forms.ValidationError(
                'Please enter a valid color.'
            )

        return color

    def clean_photo(self):

        photo = self.cleaned_data.get('photo')

        if not photo:
            return photo

        # Maximum size: 5 MB

        max_size = 5 * 1024 * 1024

        if photo.size > max_size:

            raise forms.ValidationError(
                'Photo size must be less than 5 MB.'
            )

        # Allowed image types

        allowed_types = [
            'image/jpeg',
            'image/png',
            'image/webp'
        ]

        if photo.content_type not in allowed_types:

            raise forms.ValidationError(
                'Only JPG, PNG, and WEBP images are allowed.'
            )

        return photo

    def clean_date_of_birth(self):

        date_of_birth = self.cleaned_data.get(
            'date_of_birth'
        )

        if date_of_birth:

            from datetime import date

            if date_of_birth > date.today():

                raise forms.ValidationError(
                    'Date of birth cannot be in the future.'
                )

        return date_of_birth