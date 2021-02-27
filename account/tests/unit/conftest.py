import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user_register_data():
    return {'username': 'user_name',
            'email': 'user_email',
            'password1': 'user_password',
            'password2': 'user_password'}

@pytest.fixture
def user_login_data():
    return {'username': 'user_name',
            'password': 'user_password'}


@pytest.fixture
def create_test_user(user_register_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_register_data)
    # test_user.set_password(user_data.get('password'))
    return test_user


@pytest.fixture
def authenticated_user(client, user_login_data):
    user_model = get_user_model()
    # test_user = user_model.objects.create_user(**user_data)
    # test_user.set_password(user_data.get('password'))
    # test_user.save()
    test_user = client.login(**user_login_data)
    return test_user

@pytest.fixture
def form_data():
    pass
