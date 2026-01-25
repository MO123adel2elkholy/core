import pytest
# from .your_fixture import create_test_user


@pytest.mark.django_db
def test_database_interaction(create_test_user):
    # act Phase: Use the fixture to get the test user.
    user = create_test_user
    # assert Phase: Verify the user was created correctly.
    assert user.username == 'testuser'
    assert user.check_password('password123')


# user_A is the arrange Phase fixture defined in conftest.py
def test_user_A_exists(user_A):
    # act Phase: Use the fixture to get user_A.
    user = user_A
    print("Testing with user_A:", user.username)
    # assert Phase: Verify user_A was created correctly.
    assert user.username == 'user_A'
    assert user.check_password('password123')


def test_user_is_staff_member(user_is_staff_member):
    # act Phase: Use the fixture to get user_is_staff_member.
    user = user_is_staff_member
    print("Testing with staff member:", user.username)
    # assert Phase: Verify user_is_staff_member was created correctly.
    assert user.username == 'user_B'
    assert user.is_staff is True
