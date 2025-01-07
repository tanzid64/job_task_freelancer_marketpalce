# Build and remove orphan containers
build:
	docker compose -f docker-compose.yml up --build -d --remove-orphans

# Start containers in detached mode
up:
	docker compose -f docker-compose.yml up -d

# Stop and remove containers
down:
	docker compose -f docker-compose.yml down

# Stop and remove containers and volumes
down-v:
	docker compose -f docker-compose.yml down -v

# Show logs for all services
show-logs:
	docker compose -f docker-compose.yml logs

# Show logs for the API service
show-logs-api:
	docker compose -f docker-compose.yml logs api

# Access the API shell
bash-api:
	docker exec -it freelancer_marketplace_api bash