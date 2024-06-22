from django.urls import path
from .views import ReturnTrueView

urlpatterns = [
    path('return-true/', ReturnTrueView.as_view(), name='return-true'),
]
