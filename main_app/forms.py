from django.forms import ModelForm
from .models import Match

class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ['date', 'match']