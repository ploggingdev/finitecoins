from django import forms
from django.core.validators import RegexValidator
from .models import Game, StaticResource

class AdminGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'user', 'public', 'deleted']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10}),
        }

class AdminStaticResourceForm(forms.ModelForm):
    class Meta:
        model = StaticResource
        fields = ['description', 'url', 'game', 'deleted']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10}),
        }