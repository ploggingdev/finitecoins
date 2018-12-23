from django import forms
from django.core.validators import RegexValidator
from mainapp.models import Game, StaticResource

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

class CreateGameForm(forms.Form):
    name = forms.CharField(max_length=30, validators=[RegexValidator(r'^[a-zA-Z0-9 ]+$', "Only lower case letters without spaces are allowed")])