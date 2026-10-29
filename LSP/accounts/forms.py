
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "address",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=commit)

        if commit:
            UserProfile.objects.create(
                user=user,
                role="customer",
                phone=self.cleaned_data["phone"],
                address=self.cleaned_data["address"],
            )

        return user


class ProviderRegistrationForm(CustomerRegistrationForm):
    def save(self, commit=True):
        user = super(CustomerRegistrationForm, self).save(
            commit=commit
        )

        if commit:
            UserProfile.objects.create(
                user=user,
                role="provider",
                phone=self.cleaned_data["phone"],
                address=self.cleaned_data["address"],
            )

        return user
