set -eo pipfail

COLOR_GREEN='tput setaf 2;'
COLOR_NC='tput sgr0'

echo "Starting black"
poetry run black .
echo "OK"

echo "Starting ruff"
poetry run ruff check --select I --fix
poetry run ruff check --fix
echo "ok"

echo "Starting mypy"
poetry run mypy .
echo "ok"

echo "Starting pytest with coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html
echo "ok"

echo "${COLOR_GREEN}모든 테스트가 성공적으로 완성되었습니다. ${COLOR_NC}"