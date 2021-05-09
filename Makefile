
make_migrations:
	python manage.py makemigrations

show_migrations:
	python manage.py showmigrations

deploy:
	docker-compose -f docker-compose.yml up -d --build

shutdown:
	docker-compose down

shutdown_v:
	docker-compose down -v

ps:
	docker-compose ps

logs:
	docker-compose logs ${svc}

exec:
	docker-compose exec web ${cmd}

dc_migrate:
	docker-compose exec web python manage.py migrate ${app} ${ver}

dc_show_migrations:
	docker-compose exec web python manage.py showmigrations ${app}

dc_shell:
	docker-compose exec web python manage.py shell