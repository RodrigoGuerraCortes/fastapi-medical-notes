tests: 
	docker compose exec -e PYTHONPATH=/app fastapi pytest -v --maxfail=1 --disable-warnings