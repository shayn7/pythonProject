Project structure

Project implements Page Object Model architecture.

tests: definition of test suites and scenarios:

conftest.py: allows you to define fixtures, plugins, and hooks that can be shared across multiple test files in a subdirectories.

pages: main project library combines pages construction and behaviour in page_objects, pages locator definition and generation in locators and common elements like navbars or textinputs in elements.

pytest.ini is a configuration file for Pytest that allows you to set options and modify the behavior of Pytest for a specific project.

Installation:


pip install poetry


To add a new dependency to your project, use the add command:

poetry add <package>

This will add the requests package to your project and update the pyproject.toml file.

To install dependencies defined in pyproject.toml, simply run

poetry install



Running tests:

Running all:

To run all the scripts with default setting simply type:

pytest

To run all tests and generate html report:

pytest --html=report.html

Running specific test:

pytest tests/test_main_page.py::test_main_page_loaded


This will run tests in a headed browser with a delay of 500 milliseconds between actions:

pytest --headed --slowmo 500


To run tests on specific browsers, use the Pytest command with the --browser option:

pytest --browser firefox

pytest --browser firefox --browser chromium


Other running options:

pytest --screenshot={on,off,only-on-failure}

pytest --video={on,off,retain-on-failure}
