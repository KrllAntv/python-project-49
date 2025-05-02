install: # сихронизация зависимости 
	uv sync
build: # сборка пакета
	uv build
package-install: # установка пакета
	uv tool install dist/*.whl
lint: # проверка линтера
	uv run ruff check brain_games
brain-even: # запуск игры brain-even
	uv run brain-even
brain-calc: # запуск игры brain-calcbu
	uv run brain-calc
brain-gcd: # запуск игры brain-gcd
	uv run brain-gcd
brain-progression: # запуск игры brain-progression
	uv run brain-proggression
brain-prime: # запуск игры brain-prime
	uv run brain-prime