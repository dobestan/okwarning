# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python okwarning/manage.py makemigrations proxy
	python okwarning/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls okwarning/ | grep -v -e 'manage.py' | xargs -I{} rm -rf okwarning/{}/migrations/


# target: test - execute project related tests including coding convention and unittest
test:
	flake8 okwarning/
	okwarning/manage.py test okwarning/ -v 2
