from django import forms
from .models import Images

from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['title', 'url', 'description']
        widget = {
            'url' : forms.HiddenInput
        }

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # download image from the given URL
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)

        if commit:
            image.save()
        return image


# to check if the object has a valid extensions i.e. (.png, .jpg, .jepg)
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg','png','jpeg']
        extensions =url.rsplit('.', 1)[1].lower()
        if extensions not in valid_extensions:
            raise forms.ValidationError("The given URL does not match valid image extensions.")
        return url