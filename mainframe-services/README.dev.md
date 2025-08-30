# Development Environment Setup

This guide explains how to set up and run the mainframe-services in a development environment using Docker Compose.

## Prerequisites

- Docker and Docker Compose installed
- Git

## Quick Start

### Running mainframe-services only

1. **Clone the repository and navigate to the project directory:**
   ```bash
   cd mainframe-services
   ```

2. **Set up the environment file:**
   ```bash
   cp env.dev.example .env
   ```
   
   Edit the `.env` file and update the necessary configuration values (Azure OpenAI API keys, etc.).

3. **Start the development environment:**
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

4. **Check the services:**
   ```bash
   docker-compose -f docker-compose.dev.yml ps
   ```

### Running with mainframe-workers

1. **Start mainframe-services first:**
   ```bash
   cd mainframe-services
   make dev
   ```

2. **Start mainframe-workers (in another terminal):**
   ```bash
   cd mainframe-workers
   # Modify docker-compose to use shared network (see Integration section)
   docker-compose -f docker-compose-airflow.yml up -d
   ```

## Services Included

The development environment includes the following services:

- **mainframe_services**: The main application (port 16168)
- **mainframe_worker**: Background worker for processing tasks using SAQ
- **mongodb**: Database (port 27017)
- **redis**: Cache and session storage (port 6379)
- **rabbitmq**: Message queue with management UI (ports 5672, 15672)

## Network Configuration

The services run on a shared network called `mainframe-dev-network` which allows other repositories (like mainframe-workers) to connect to these services.

### Connecting Other Repositories

To connect the mainframe-workers repository to this network:

```bash
# From the mainframe-workers directory
docker network connect mainframe-dev-network mainframe-workers
```

Or if you're running mainframe-workers with its own docker-compose:

```yaml
# In mainframe-workers docker-compose.yml
networks:
  default:
    external:
      name: mainframe-dev-network
```

## Environment Variables

### Development vs Production

- **Development**: Uses `env.dev.example` with Docker service names (mongodb, redis, rabbitmq)
- **Production**: Uses `env.example` with localhost or external service endpoints

### Key Differences in Development

```bash
# Development (Docker Compose)
MONGO_HOST="mongodb"
REDIS_URL="redis://redis:6379/0"
RABBITMQ_HOST="rabbitmq"

# Production (External services)
MONGO_HOST="localhost"
REDIS_URL="redis://localhost:6379/0"
RABBITMQ_HOST="localhost"
```

## Useful Commands

### Start services
```bash
docker-compose -f docker-compose.dev.yml up -d
```

### Stop services
```bash
docker-compose -f docker-compose.dev.yml down
```

### View logs
```bash
# All services
docker-compose -f docker-compose.dev.yml logs -f

# Specific service
docker-compose -f docker-compose.dev.yml logs -f mainframe_services

# Worker logs
docker-compose -f docker-compose.dev.yml logs -f mainframe_worker
```

### Rebuild and restart
```bash
docker-compose -f docker-compose.dev.yml up -d --build
```

### Start worker only
```bash
make dev-worker
```

### Clean up (removes volumes)
```bash
docker-compose -f docker-compose.dev.yml down -v
```

## Access Points

- **Mainframe Services API**: http://localhost:16168
- **RabbitMQ Management**: http://localhost:15672 (admin/dev_password)
- **MongoDB**: localhost:27017
- **Redis**: localhost:6379

## Troubleshooting

### Port Conflicts
If you get port conflicts, check if other services are using the same ports:
- 16168 (mainframe services)
- 27017 (MongoDB)
- 6379 (Redis)
- 5672 (RabbitMQ)
- 15672 (RabbitMQ Management)

### Database Connection Issues
Ensure the MongoDB initialization script (`init-mongo.js`) is properly set up and the credentials match your `.env` file.

### Network Issues
If other repositories can't connect to the services, verify the network exists:
```bash
docker network ls | grep mainframe-dev-network
```

## Development Workflow

1. Start the development environment
2. Make code changes in the `app/` directory
3. The changes are automatically reflected due to volume mounting
4. Restart services if needed: `docker-compose -f docker-compose.dev.yml restart mainframe_services`

## Integration with mainframe-workers

The mainframe-workers repository runs its own Airflow setup. To integrate both services:

### Option 1: Use Shared Services (Recommended)
1. Start mainframe-services first: `make dev`
2. In mainframe-workers, modify the docker-compose to use the shared network:
   ```yaml
   # In mainframe-workers docker-compose-airflow.yml
   networks:
     default:
       external:
         name: mainframe-dev-network
   ```
3. Remove Redis and MongoDB services from mainframe-workers docker-compose
4. Update environment variables in mainframe-workers to use:
   - `REDIS_URL=redis://redis:6379/0`
   - `MONGO_HOST=mongodb`

### Option 2: Run Independently
1. Start mainframe-services: `make dev`
2. Start mainframe-workers with its own services
3. Connect the networks manually:
   ```bash
   docker network connect mainframe-dev-network <mainframe-workers-container>
   ```

### Shared Network Benefits
- Both services can communicate with each other
- Shared Redis instance reduces resource usage
- Shared MongoDB instance for consistent data
- RabbitMQ available for message queuing between services
