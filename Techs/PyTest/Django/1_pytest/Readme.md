# How to Setup PyTest

1. Create tests folder on each app, pytest.ini (populate with basic setup) , conftest.py (contains common fixtures ) in project root dir.
2. Set DJANGO_SETTINGS_MODULE in pytest.ini as per project name
3. run pytest -v --ds=${DJANGO_SETTINGS_MODULE} etc. command from Makefile

### Try avoid tests.py, use test_*.py *_tests.py
### class TestViews() => class name styles


Later : Cover all  +  DRF :
https://djangostars.com/blog/django-pytest-testing/


References:
* [pytest-django.readthedocs](https://pytest-django.readthedocs.io/en/latest/database.html)

PyTest Plugins:
https://docs.pytest.org/en/latest/reference/plugin_list.html


# Summary Command:
Executing all test files using pytest –v.
Executing specific file usimng pytest <filename> -v.
Execute tests by substring matching pytest -k <substring> -v.
Execute tests based on markers pytest -m <marker_name> -v.
Creating fixtures using @pytest.fixture.
conftest.py allows accessing fixtures from multiple files.
Parametrizing tests using @pytest.mark.parametrize.
Xfailing tests using @pytest.mark.xfail.
Skipping tests using @pytest.mark.skip.
Stop test execution on n failures using pytest --maxfail = <num>.
Running tests in parallel using pytest -n <num>.
Generating results xml using pytest -v --junitxml = "result.xml".
pytest a_directory                     # directory
pytest test_something.py               # tests file
pytest test_something.py::single_test  # single test function
pytest -m "xfail and not slow" --strict-markers 