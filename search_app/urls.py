from django.urls import path
from .  import views
from django.urls import reverse
app_name= 'search_app'

urlpatterns = [
    path('',views.SearchResult,name='SearchResult'),
    ]
