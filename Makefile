install: # сихронизация зависимости 
	uv sync
brain-games: # запуск игры
	uv run brain-games
build: # сборка пакета
	uv build
package-install: # установка пакета
	uv tool install dist/*.whl