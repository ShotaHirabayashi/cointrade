from django.urls import path
from .views import IndexTemplateView,coinfunc

app_name = 'finchart'

urlpatterns = [
    path('', coinfunc, name='index'),
]