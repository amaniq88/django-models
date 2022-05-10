from django.urls import URLPattern, path
from .views import SnackListview

urlpatterns = [
    path('snack_list', SnackListview.as_view(), name='snack_list')
]