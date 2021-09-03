from django.contrib import admin
from .models import predicted_score, nfl_teams
# Register your models here.
admin.site.register(predicted_score)
admin.site.register(nfl_teams)