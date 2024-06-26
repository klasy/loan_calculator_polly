from django.urls import path

from .views import LoanListCreateAPIView, LoanRetrieveAPIView

urlpatterns = [
    path('loans/', LoanListCreateAPIView.as_view(), name='loan-list'),
    path('loans/<int:pk>/', LoanRetrieveAPIView.as_view(), name='loan-detail'),
]
