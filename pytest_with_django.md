# Pytest with Django
This document provides guidance on how to use Pytest with Django for testing your applications.
## Installation
To get started, you need to install `pytest` and `pytest-django`. You can do this using pip:
```bash
pip install pytest pytest-django
```
## Configuration
Create a `pytest.ini` file in the root of your Django project with the following content:
```ini
[pytest]
DJANGO_SETTINGS_MODULE = your_project_name.settings
python_files = tests.py test_*.py *_tests.py
```
Replace `your_project_name` with the actual name of your Django project.
## Writing Tests
You can write your tests in the `tests.py` file or create a separate `tests` directory. Here is an example of a simple test case:
```pythonimport pytest
from django.urls import reverse
from django.test import Client
@pytest.mark.django_db
def test_homepage():
    client = Client()
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
```
## Running Tests
To run your tests, simply execute the following command in your terminal:
```bashpytest
```
pytest
```


This will discover and run all the tests in your project.
## Additional Features
Pytest offers several features that can enhance your testing experience:
- Fixtures: Use fixtures to set up test data and state.
- Parametrization: Run a test with multiple sets of parameters.
- Plugins: Extend Pytest functionality with various plugins available in the community.
For more information, refer to the [pytest-django documentation](https://pytest-django.readthedocs.io/en/latest/).
```python
```


# Conclusion
Using Pytest with Django can significantly improve your testing workflow. With its powerful features and ease of use, you can write effective tests for your Django applications.
Using Pytest with Django can significantly improve your testing workflow. With its powerful features and ease of use, you can write effective tests for your Django applications.

if __name__ == "__main__":
    print("This is a documentation file for using Pytest with Django.")


if you want to stop testing after the first failure, you can use the `-x` option:
bashpytest -x



if you want to run tests in parallel, you can use the `pytest-xdist` plugin:
bashpip install pytest-xdist
pytest -n auto

if you want to generate a test coverage report, you can use the `pytest-cov` plugin:
bashpip install pytest-cov

pytest --cov=your_app_name

if you want to run tests with a specific marker, you can use the `-m` option:
bashpytest -m your_marker


if you want to run tests in a specific file or directory, you can specify the path:
bashpytest path/to/your/tests
bashpytest --cov=your_app_name

if you want to run tests with a specific marker, you can use the `-m` option:
bashpytest -m your_marker



if  you have print statements in your tests and want to see their output, you can use the `-s` option
bashpytest -s

# apattern for writting tests 
1- arrange: set up the conditions for the test
2-act: perform the action being tested
3- assert: verify the outcome

# Arrange-Act-Assert Pattern Example
```pythonpython
import pytest
from django.urls import reverse
from django.test import Client
from myapp.models import MyModel
@pytest.mark.django_db
def test_create_mymodel():
    # Arrange
    client = Client()
    url = reverse('create_mymodel')
    data = {'name': 'Test Model', 'description': 'This is a test model.'}
    
    # Act
    response = client.post(url, data)
    
    # Assert
    assert response.status_code == 201
    assert MyModel.objects.filter(name='Test Model').exists()
```

# Common Pytest Command-Line Options
- `-x`: Stop after the first failure.
- `-n auto`: Run tests in parallel using all available CPU cores (requires `pytest-xdist`).
- `--cov=your_app_name`: Generate a coverage report for the specified app (requires `pytest-cov`).

# wahat is pytest fixtures
Pytest fixtures are a way to provide a fixed baseline upon which tests can reliably and repeatedly execute. They are used to set up the necessary state or context for tests, such as creating test data, configuring settings, or initializing resources.
They are defined using the `@pytest.fixture` decorator and can be used in test functions by including them as parameters.
# Example of a Pytest Fixture
```pythonpython
import pytest
from myapp.models import MyModel
@pytest.fixture
def mymodel_fixture(db):
    # Set up test data
    mymodel = MyModel.objects.create(name='Fixture Model', description='This is a fixture model.')
    return mymodel
@pytest.mark.django_db
def test_mymodel_using_fixture(mymodel_fixture):
    # Use the fixture in the test
    assert mymodel_fixture.name == 'Fixture Model'
    assert MyModel.objects.count() == 1
```
# Using Fixtures in Tests
You can use fixtures in your tests by simply adding them as parameters to your test functions. Py
test will automatically look for fixtures with matching names and provide them to the test.
Fixtures can also depend on other fixtures, allowing you to build complex setups in a modular way.
fixture runs once per test function by default, but you can change this behavior using the `scope` parameter in the `@pytest.fixture` decorator (e.g., `function`, `class`, `module`, `session`).
for example, to create a fixture that runs once per module:
```pythonpython
import pytest
from myapp.models import MyModel
@pytest.fixture(scope='module')
def mymodel_module_fixture(db):
    # Set up test data
    mymodel = MyModel.objects.create(name='Module Fixture Model', description='This is a module fixture model.')
    return mymodel
@pytest.mark.django_db
def test_mymodel_module_using_fixture(mymodel_module_fixture):
    # Use the fixture in the test
    assert mymodel_module_fixture.name == 'Module Fixture Model'
    assert MyModel.objects.count() == 1
```




# waht is conftest.py
`conftest.py` is a special configuration file used by Pytest to define fixtures and other configurations that are shared across multiple test files within a directory.
It allows you to organize and reuse fixtures without needing to import them explicitly in each test file.
# Example of conftest.py
```pythonpython
import pytest
from django.contrib.auth.models import User
@pytest.fixture
def test_user(db):
    # Create a test user
    user = User.objects.create_user(
        username='testuser', password='password123')
    print("Test user created with username:", user.username)
    return user
```

# we use fixtures as factory functions to create different test data  according to our test needs
```pythonpython
import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user_factory_fixture(db):
    # arrange Phase: Factory function to create users with different attributes.
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

```

# What is the Factory Method Pattern
The Factory Method Pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
In the context of testing with Pytest, using fixtures as factory functions allows you to create different test data according to your test needs, similar to how the Factory Method Pattern allows for the creation of objects based on specific requirements.


# What is a Factory
A factory is a function or class that creates objects. In the context of testing with Pytest, a factory function is a fixture that returns a function capable of creating test data.

# Factory Boy With Django and Pytest
Factory Boy is a popular library for creating test data in Python. It provides a way to define factories for your models, allowing you to easily create instances of your models with predefined attributes

# Example of Factory Boy
```pythonpython
import factory
from myapp.models import MyModel
class MyModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MyModel

    name = factory.Faker('name')
    description = factory.Faker('text')
```


<!-- according to Design Patterns Factory Method  Pattern -->
# Conclusion
Using Pytest fixtures can help you write cleaner and more maintainable tests by separating setup code from test logic. They also promote reusability and consistency across your test suite. test will automatically look for fixtures with matching names and provide them to the test.
test will automatically look for fixtures with matching names and provide them to the test.




