from django.urls import path
from .views import SearchByKeyWord

urlpatterns = [
    path("<str:keyword>/", SearchByKeyWord, name="search_products"),
]
