from mixer.backend.django import mixer
import pytest
from account.models import UserAuth


@pytest.mark.django_db
class TestModels:

    def test_user_auth(self):
        user = mixer.blend(UserAuth, username='test user', nutriscore='a')
        assert user.username == 'test user'
        assert UserAuth.objects.filter(username='test user').exists() is True
