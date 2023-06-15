from django.contrib import admin
from django.urls import path, include
from calculator.views import LoanListCreateView, LoanRetrieveView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Loans/', LoanListCreateView.as_view(), name='Loan-list'),
    path('api/Loans/<int:pk>/', LoanRetrieveView.as_view(), name='Loan-detail'),
    path('api-auth/', include('rest_framework.urls')),
]
