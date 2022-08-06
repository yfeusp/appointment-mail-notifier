PYTHON_VER = python3.9

# Create venv with explicit Python version, otherwise pipenv uses highest
setup:
	pipenv --python ${PYTHON_VER} sync --dev

# Can be used to update installed dependencies after venv already created
install-dependencies:
	pipenv sync --dev

setup-pipenv-shell: install-dependencies
	pipenv shell

code-analysis:
	pipenv run flake8  .

black:
	pipenv run black --line-length 79 .

test:
	pipenv run pytest

start:
	pipenv run app

tests-coverage:
	pipenv run tests-coverage

