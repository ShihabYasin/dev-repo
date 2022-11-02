from django.urls import path
from .views import CustomerCreate, CustomerList, CustomerDetail, CustomerUpdate, CustomerDelete

app_name = 'api'

urlpatterns = [
    path('customer/create/', CustomerCreate.as_view(), name='create-customer'),
    path('customer/retrive/<int:pk>/', CustomerDetail.as_view(), name='retrieve-customer'),
    path('customer/update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    path('customer/delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer'),
    path('customer/list', CustomerList.as_view()),
]