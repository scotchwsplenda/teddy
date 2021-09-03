
from .models import predicted_score, nfl_teams
from django.forms import ModelForm

class prediction_form(ModelForm):
    class Meta:
        model = predicted_score
        fields = '__all__'
        exclude = ('team', 'submitted_date')
