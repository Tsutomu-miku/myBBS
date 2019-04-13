from django import forms
from django.core.files.base import ContentFile 
from slugify import slugify
from urllib import request
from .models import Image

# header={
#      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
#      "referer":"https://image.baidu.com"
#     }


class ImageForm(forms.ModelForm):
    class Meta: 
        model = Image
        fields = ('title', 'url', 'description')

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError("The given Url does not match valid image extension.")
        return url
    
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageForm, self).save(commit=False)

        image_url = self.cleaned_data['url']
        # rep=request.Request(image_url,headers=header)

        image_name = '{0}.{1}'.format(slugify(image.title), image_url.rsplit('.', 1)[1].lower()) 
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save() 
        
        return image