docker compose up -d --build

sleep 8
docker exec django_pokemon_example-api-1 python /src/manage.py makemigrations
docker exec django_pokemon_example-api-1 python /src/manage.py migrate