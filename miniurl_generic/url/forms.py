# coding: utf-8
from django import forms
from models import MiniUrl

class UrlForm(forms.ModelForm):
    class Meta:
        model = MiniUrl
        fields= [
            'pseudo',
            'url_complete',
        ]
