from django.test import Client
import pytest

from pytest_app.models import Customer 
from django.utils import timezone


def test_page():
    client = Client()
    response = client.get('/home/')
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_db_object():
    # cliens_cnt  = Customer.objects.get(name='C-1')
    Customer.objects.create(
        name = 'C-3',
        email = 'C3@gmail.com',
        created = timezone.now()
    )

    assert Customer.objects.filter(email ='C3@gmail.com').exists() == True
    
    