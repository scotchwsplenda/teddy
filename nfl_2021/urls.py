from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('cool_form/', views.choose_team_view),
    path('cool_form/<acr>/', views.cool_form_view, name='cool_form_team'),
    path('', TemplateView.as_view(template_name='nfl_2021/home.html')),
    path('results/', views.choose_results_view),
    path('results/<acr>', views.results_view, name='results_team'),
    path('accuracy/', views.choose_accuracy_view),
    path('accuracy/<acr>', views.diffy_view, name='diffy_view_name'),
    

]