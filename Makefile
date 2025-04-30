install: # сихронизация зависимости 
	uv sync
brain-games: # запуск игры
	uv run brain-games
build: # сборка пакета
	uv build
package-install: # установка пакета
	uv tool install dist/*.whl
lint: # проверка линтера
	uv run ruff check brain_games
brain-even: # запуск игры brain-even
	uv run brain-even