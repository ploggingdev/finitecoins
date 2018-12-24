from django import forms
from django.core.validators import RegexValidator
from mainapp.models import Game, StaticResource
import markdown
import bleach
from bs4 import BeautifulSoup
from django.conf import settings

class AdminGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'description_html', 'user', 'public', 'deleted']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10}),
        }

    def clean(self):
        description = self.cleaned_data['description']
        description_html = markdown.markdown(description)
        description_html = bleach.clean(description_html, tags=settings.COMMENT_TAGS, strip=True)
        soup = BeautifulSoup(description_html, "html.parser")
        for i in soup.find_all('a'):
            i['target'] = '_blank'
            i['rel'] = 'noopener noreferrer nofollow'
        for i in soup.find_all('blockquote'):
            i['class'] = 'blockquote'
        description_html = soup.prettify()

        self.cleaned_data['description_html'] = description_html

        return self.cleaned_data

class AdminStaticResourceForm(forms.ModelForm):
    class Meta:
        model = StaticResource
        fields = ['description', 'url', 'game', 'deleted']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10}),
        }

class CreateGameForm(forms.Form):
    name = forms.CharField(max_length=30, validators=[RegexValidator(r'^[a-zA-Z0-9 ]+$', "Only lower case letters without spaces are allowed")])

class DevGameDescriptionForm(forms.Form):
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows': 10}))