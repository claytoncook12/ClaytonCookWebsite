# www.claytoncook.com

This is a personal website that uses Django.

## Docker commands to build and run docker containers

Build the needed files for the Postgres database and shut back down. Will be  in `DjangoApp/data` when run. 
```
docker compose -f docker-compose.dev.yml up -d db
docker compose -f docker-compose.dev.yml down db
```

Now the database files are created and can run all containers.
```
docker compose -f docker-compose.dev.yml up -d
```