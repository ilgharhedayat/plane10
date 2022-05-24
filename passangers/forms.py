from django import forms
from django.forms import formset_factory, modelformset_factory

from .models import Passenger


class PassengerForm(forms.ModelForm):
    url = forms.URLField()
    day = forms.CharField(label="")
    month = forms.CharField(label="")
    year = forms.CharField(label="")

    class Meta:
        model = Passenger
        fields = (
            "en_name",
            "en_family",
            "gender",
            "national_code",
            "ir_name",
            "day",
            "month",
            "year ",
        )
        widgets = {
            "en_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "نام لاتین ",
                }
            ),
            "en_family": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "نام خانوادگی لایتن",
                }
            ),
            "gender": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "جنسیت",
                }
            ),
            "national_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "کد ملی",
                }
            ),
            "ir_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelGoal",
                    "placeholder": "نام",
                }
            ),
        }


GeeksFormSet = modelformset_factory(PassengerForm, extra=4)

from django import forms


class LinkForm(forms.Form):
    anchor = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Link Name / Anchor Text",
            }
        ),
        required=False,
    )
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder": "URL",
            }
        ),
        required=False,
    )


class ProfileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields["first_name"] = forms.CharField(
            max_length=30,
            initial=self.user.first_name,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "First Name",
                }
            ),
        )
        self.fields["last_name"] = forms.CharField(
            max_length=30,
            initial=self.user.last_name,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Last Name",
                }
            ),
        )


from django.forms.formsets import BaseFormSet


class BaseLinkFormSet(BaseFormSet):
    def clean(self):

        if any(self.errors):
            return

        anchors = []
        urls = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                anchor = form.cleaned_data["anchor"]
                url = form.cleaned_data["url"]

                if anchor and url:
                    if anchor in anchors:
                        duplicates = True
                    anchors.append(anchor)

                    if url in urls:
                        duplicates = True
                    urls.append(url)

                if duplicates:
                    raise forms.ValidationError(
                        "Links must have unique anchors and URLs.",
                        code="duplicate_links",
                    )

                if url and not anchor:
                    raise forms.ValidationError(
                        "All links must have an anchor.", code="missing_anchor"
                    )
                elif anchor and not url:
                    raise forms.ValidationError(
                        "All links must have a URL.", code="missing_URL"
                    )
