### Align local mainframe-services with local Airflow (mainframe-workers)

This spec describes how to run `mainframe-services` (this repo) together with the Airflow stack from `mainframe-workers` so they work seamlessly in local development.

#### TL;DR
- Start `mainframe-services` with: `make dev` (creates network `mainframe-dev-network` and brings up API + MongoDB + Redis + RabbitMQ).
- In `mainframe-workers`, connect to that same docker network and use the shared Redis/MongoDB (recommended), or run in isolation.
- Prefer shared services to avoid port conflicts and to keep data in one place during dev.

---

### 1) What mainframe-services exposes locally

From `docker-compose.dev.yml` in this repo:
- Network: `mainframe-dev-network` (bridge)
- Services:
  - API: `mainframe_services` on host `localhost:16168` (inside network: `mainframe_services:8000`)
  - MongoDB: service name `mongodb` (exposed internally only, port 27017)
  - Redis: service name `redis` (exposed internally only, port 6379)
  - RabbitMQ: service name `rabbitmq` (exposed internally only, port 5672; management 15672 internal)

Environment alignment for the API (already set in `env.dev.example` and compose):
- MONGO_HOST=`mongodb`
- REDIS_URL=`redis://redis:6379/0`
- RABBITMQ_HOST=`rabbitmq`

---

### 2) Recommended: Use shared MongoDB/Redis from mainframe-services in Airflow stack

In the `mainframe-workers` repo (Airflow compose snippet you shared), align it to the shared network and shared services.

Steps:
1. Ensure `mainframe-services` is running:
   - `cd mainframe-services && make dev`

2. In `mainframe-workers`, set the default network to the shared one:
   ```yaml
   # docker-compose-airflow.yml (mainframe-workers)
   networks:
     default:
       external:
         name: mainframe-dev-network
   ```

3. Remove/disable local Redis/MongoDB from the Airflow compose, OR rename them to avoid conflicts. If you remove them, Airflow will use the existing ones from `mainframe-services` via DNS names `redis` and `mongodb`.

   - If you keep them, you must change names/ports to avoid clashes; not recommended.

4. Keep Airflow Redis broker URL as:
   ```
   AIRFLOW__CELERY__BROKER_URL=redis://:@redis:6379/0
   ```
   This resolves to the shared `redis` on `mainframe-dev-network`.

5. MongoDB usage (if your DAGs or workers read/write Mongo):
   - Use host `mongodb`, port `27017`, and the same credentials you use in `mainframe-services`.
   - In `.env` for workers, mirror:
     - `MONGO_INITDB_ROOT_USERNAME=admin`
     - `MONGO_INITDB_ROOT_PASSWORD=<your dev pwd>`
     - `MONGO_INITDB_DATABASE=mainframe`

6. Start Airflow:
   - `docker compose -f docker-compose-airflow.yml up -d`

7. If containers are already running and not on the network, connect them manually:
   ```bash
   docker network connect mainframe-dev-network <airflow-container-name>
   ```

---

### 3) Alternative: Run Airflow with its own Redis/MongoDB (isolated mode)

If you prefer isolation:
- Keep `redis` and `mongodb` services in the Airflow compose as is.
- To avoid host port conflicts:
  - Remove host port bindings (only use `expose`) or change to different host ports.
  - Example for Redis in Airflow: remove `ports: ["6379:6379"]` and keep `expose: [6379]`.
- Do not join the `mainframe-dev-network` in this mode, or ensure service names are distinct (`airflow-redis`, `airflow-mongodb`).

Trade-offs:
- Pros: No dependency on `mainframe-services` stack.
- Cons: Duplicate services, higher resource usage, split data.

---

### 4) Health checks and common pitfalls

- The API uses `uvicorn` live reload and mounts `./app` to `/workspace/app`.
- The API does not expose a `/health` route by default. If you want health checks green, either:
  - Add a `GET /health` endpoint returning 200, or
  - Update the healthcheck path to an existing route.
- RabbitMQ is internal-only in dev to avoid host port conflicts. Airflow uses Redis for Celery by default, so RabbitMQ is not required for Airflow.

Port conflicts you might see:
- `27017` (Mongo), `6379` (Redis), `5672`/`15672` (RabbitMQ). In this spec, we avoid binding those to the host in dev; they’re available on the shared network.

---

### 5) Quick commands

Mainframe services:
```bash
cd mainframe-services
make dev           # up
make dev-logs      # tail logs
make dev-down      # down
```

Airflow stack (mainframe-workers):
```bash
cd mainframe-workers
docker compose -f docker-compose-airflow.yml up -d
docker compose -f docker-compose-airflow.yml logs -f --tail=100
```

Joining a running container to the shared network:
```bash
docker network connect mainframe-dev-network <container-name>
```

---

### 6) Expected environment alignment

In `mainframe-services/.env` (or `env.dev.example` copied to `.env`):
```
MONGO_HOST=mongodb
MONGO_PORT=27017
MONGO_USER=admin
MONGO_PASSWORD=<dev password>
MONGO_DATABASE=mainframe
REDIS_URL=redis://redis:6379/0
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_USER=admin
RABBITMQ_PASSWORD=<dev password>
RABBITMQ_VHOST=/
```

In `mainframe-workers/.env` (if reading shared services):
```
AIRFLOW__CELERY__BROKER_URL=redis://:@redis:6379/0
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=<dev password>
MONGO_INITDB_DATABASE=mainframe
```

This ensures both stacks resolve `redis` and `mongodb` DNS names on the shared `mainframe-dev-network` and reuse the same data stores locally.


