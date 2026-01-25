import email
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
# Additional fixtures can be added here as needed for other tests.

# We can use fixcure as afactory to create multiple users with different attributes.


@pytest.fixture
def user_factory_fixture(db):
    # arrange Phase: Factory function to create users with different attributes.
    # nested function to create users
    def create_app_user(username, password: str = 'password123',
                        first_name: str = 'first',
                        last_name: str = 'last',
                        email: str = 'email@example.com',
                        is_staff: bool = False, is_superuser: bool = False, is_active: bool = True):
        user = User.objects.create_user(
            username=username, password=password, first_name=first_name, last_name=last_name, email=email,
            is_staff=is_staff, is_superuser=is_superuser, is_active=is_active)
        print("Test user created with username:", user.username)
        return user

    return create_app_user


@pytest.fixture
def user_A(db, user_factory_fixture):
    return user_factory_fixture(username='user_A', password='password123')


@pytest.fixture
def user_is_staff_member(db, user_factory_fixture):
    return user_factory_fixture(username='user_B', password='password123', is_staff=True)
