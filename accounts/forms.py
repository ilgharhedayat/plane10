from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import ValidationError

from .models import User, UserDocument


class CreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "user_name",
            "email",
            "phone_number",
        )

    def clean(self):
        clean_data = super(CreationForm, self).clean()
        password = clean_data.get("password")
        password_confirm = clean_data.get("password_confirm")
        if (password and password_confirm) and (password != password_confirm):
            raise ValidationError("un match password")
        return password

    def save(self, commit=True):
        user = super(CreationForm, self).save()
        user.set_password(self.changed_data["password"])
        if commit:
            user.save()
        return user


class ChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "user_name",
            "email",
            "phone_number",
            "password",
        )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "travelSrc",
                "placeholder": "کلمه عبور",
            }
        )
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "travelSrc",
                "placeholder": "تکرار کلمه عبور",
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "user_name",
            "email",
            "phone_number",
        )
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "id": "travelSrc", "placeholder": "نام"}
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "نام خانوادگی",
                }
            ),
            "user_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "نام کاربری",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "شماره تلفن",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelGoal",
                    "placeholder": "Email",
                }
            ),
        }

    # def clean(self):
    #     clean_data = super(RegisterForm, self).clean()
    #     password = clean_data["password"]
    #     password_confirm = clean_data["password_confirm"]
    #     if (password and password_confirm) and (password != password_confirm):
    #         raise ValidationError("un match password")
    #     return password


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("user_name", "password")
        widgets = {
            "user_name": forms.TextInput(
                attrs={"class": "form-control", "id": "travelSrc", "placeholder": ""}
            ),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "id": "travelSrc", "placeholder": ""}
            ),
        }


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "id": "travelSrc", "placeholder": ""}
        )
    )


class UserDocumentForm(forms.ModelForm):
    class Meta:
        model = UserDocument
        fields = (
            'national_card',
            'identity_card',
            'passport',
            'other',
        )
        widgets = {
            "national_card": forms.FileInput(
                attrs={"class": "form-control", "id": "travelSrc", "placeholder": ""}
            ),
            "identity_card": forms.FileInput(
                attrs={"class": "form-control", "id": "travelSrc", "placeholder": ""}
            ),

            "passport": forms.FileInput(
                attrs={"class": "form-control", "id": "travelSrc", "placeholder": ""}
            ),

            "other": forms.FileInput(
                attrs={"class": "form-control", "id": "travelSrc", "placeholder": ""}
            ),
        }
