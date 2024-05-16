from django.forms import ModelForm
from django import forms
from .models import Upload


class UploadForms(ModelForm):
    name = forms.TextInput()
    tel_number = forms.TextInput()
    number_product = forms.TextInput()

    class Meta:
        model = Upload
        fields = ['name', 'tel_number', 'number_product']

    def __init__(self, *args, **kwargs):
        super(UploadForms, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input100'})
        self.fields['tel_number'].widget.attrs.update({'class': 'input100'})
        self.fields['number_product'].widget.attrs.update({'class': 'input100'})