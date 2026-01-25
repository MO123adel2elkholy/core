from django.contrib.auth.models import User
import pytest


# arrange Phase: Set up any necessary preconditions or inputs.
@pytest.fixture
def create_test_user(db):
    """
    Fixture to create a test user in the database.
    """
    user = User.objects.create_user(
        username='testuser', password='password123')
    print("Test user created with username:", user.username)
    return user
