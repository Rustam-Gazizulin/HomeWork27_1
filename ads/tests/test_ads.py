import json

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_create_ad(api_client, user):
    data = {
        'name': 'class198723',
        'author': user.id,
        'price': 10,
    }
    res = api_client.post(
        '/ad/',
        data=json.dumps(data),
        content_type='application/json',
    )
    res_data = res.json()
    assert res_data['name'] == data['name']
    assert res_data['price'] == data['price']
    assert res_data['author'] == data['author']


@pytest.mark.django_db
def test_list_ads(api_client):
    res = api_client.get('/ad/')
    assert res.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_ad_by_id(api_client, ad):
    res = api_client.get(f'/ad/{ad.pk}/')
    assert res.status_code == status.HTTP_200_OK
    assert res.json()['id'] == ad.id
