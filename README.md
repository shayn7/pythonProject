Project structure
Project implements Page Object Model architecture.

tests: definition of test suites and scenarios

conftest.py: allows you to define fixtures, plugins, and hooks that can be shared across multiple test files in a subdirectories.

pages: main project library combines pages construction and behaviour in page_objects, pages locator definition and generation in locators and common elements like navbars or textinputs in elements.

pytest.ini is a configuration file for Pytest that allows you to set options and modify the behavior of Pytest for a specific project.

Installation
Poetry is a dependency management and packaging tool for Python that helps you manage your project's dependencies and build your project. It's similar to pip, but provides additional features and benefits.

Installation using poetry
Installing Poetry
Poetry can be installed via python standard package manager PIP

pip install poetry

Adding dependencies
To add a new dependency to your project, use the add command:

poetry add <package>

This will add the requests package to your project and update the pyproject.toml file.

Installing dependencies
To install dependencies defined in pyproject.toml, simply run

poetry install

Running tests
This project uses pytest with pytest-playwright as a test runner.

Defining test choice
Running all
To run all the scripts with default setting simply type:

pytest

Running specific test
pytest tests/test_main_page.py::test_main_page_loaded

Developer friendly run commands
This will run tests in a headed browser with a delay of 500 milliseconds between actions. It will make observing browser behaviour easier.

pytest --headed --slowmo 500

Running Tests on Specific Browsers
To run tests on specific browsers, use the Pytest command with the --browser option:

pytest --browser firefox
This will run tests on Firefox. You can also specify multiple browsers:

pytest --browser firefox --browser chromium

Other running options

Playwright comes with video recording and screen capturing out of the box. The results are saved in test-results directory by default.

pytest --screenshot={on,off,only-on-failure}

pytest --video={on,off,retain-on-failure}