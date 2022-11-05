from django.test import Client
import pytest

from pytest_app.models import Customer 
from django.utils import timezone


class TestViews():
    
    # def test_page(self):
    #     client = Client()
    #     response = client.get('/home/')
    #     assert response.status_code == 200
    # above is default Django styled OR like below with pytest
        
    @pytest.mark.django_db
    def test_index(self, client): # getting default browser "client" from pytest 
        response = client.get('/home/')
        assert response.status_code == 200
            
    @pytest.mark.django_db
    def test_db_object(self):
        # cliens_cnt  = Customer.objects.get(name='C-1')
        Customer.objects.create(
            name = 'C-3',
            email = 'C3@gmail.com',
            created = timezone.now()
        )

        assert Customer.objects.filter(email ='C3@gmail.com').exists() == True
        

    @pytest.mark.django_db
    @pytest.mark.parametrize('different_views', ['home', 'index'])
    def test_detail_views(self, different_views):
        client = Client()
        response = client.get('/{}/'.format(different_views))
        assert response.status_code == 200