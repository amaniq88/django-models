from django.urls import  path
from .views import SnackListview, snackDetailView

urlpatterns = [
    path('snack_list', SnackListview.as_view(), name='snack_list'),
    path('snack_detail/<int:pk>', snackDetailView.as_view(), name='snack_detail'),

]