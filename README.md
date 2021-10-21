# www.claytoncook.com

This is a personal website that uses Django.

## Docker commands to build and run docker containers

Build the needed files for the Postgres database and shut back down. Will be  in `DjangoApp/data` when run. 
```
docker compose -f docker-compose.dev.yml up -d db
```

Now you can run the Django development server
```
python DjangoApp\manage.py runserver
```
