# Airflow Workers Guide for Local Development

This guide explains how to run Airflow workers using Docker and manage DAGs for mainframe parsing workflows.

**Current Airflow Version: 2.10.5**

## Quick Start

### 1. Start Airflow Services
```bash
# Build and start all Airflow services
docker compose -f docker-compose-airflow.yaml up --build

# Start in background
docker compose -f docker-compose-airflow.yaml up -d

# Access Airflow UI
open http://localhost:8080
```

**Default Login:**
- Username: `airflow`
- Password: `airflow`

You can change username and password in the .env file by changing
`_AIRFLOW_WWW_USER_USERNAME` and `_AIRFLOW_WWW_USER_PASSWORD`

**Database connection:**

The worker requires a connection to MongoDB. You need to add the network of Airflow container to the MongoDB container.

1. Get the Network Name of Airflow container:

```bash
docker network ls
```

The network name can be `mainframe-workers_default` if you use the default network name.

2. Add the network to the MongoDB container:

```bash
docker network connect mainframe-workers_default mongodb
```

### 2. Stop Airflow Services
```bash
# Stop all services
docker compose -f docker-compose-airflow.yaml down

# Stop and remove volumes (clean slate)
docker compose -f docker-compose-airflow.yaml down --volumes
```

## Services Overview

| Service | Port | Description |
|---------|------|-------------|
| airflow-webserver | 8080 | Web UI for managing DAGs |
| airflow-scheduler | - | Schedules and triggers DAG runs |
| airflow-worker | - | Executes tasks |
| postgres | 5432 | Database backend |
| redis | 6379 | Message broker for Celery |

## DAG Management

### Directory Structure
```
dags/
├── reverse_repo_dag.py          # Main repository processing DAG
└── __pycache__/                 
```

### Adding a New DAG

1. **Create DAG file in `dags/` directory:**
```python
# dags/my_new_dag.py
import sys
from datetime import timedelta
from airflow import DAG
from airflow.decorators import task
from airflow.models.param import Param

sys.path.append("./src")  # Required for importing src modules

with DAG(
    dag_id="my_new_dag",
    schedule=None,  # Manual trigger only
    params={
        "input_param": Param(
            type="string",
            description="Description of the parameter"
        ),
    },
    default_args={
        "execution_timeout": timedelta(seconds=3600),
    },
    description="Description of what this DAG does",
    tags=["tag1", "tag2"],  # Optional tags for organization
) as dag:
    
    @task.python()
    def my_task(**context):
        """Task description"""
        input_param = context["params"]["input_param"]
        
        # Your task logic here
        print(f"Processing: {input_param}")
        
        return {"status": "success", "result": "some_result"}
    
    @task.python()
    def another_task(upstream_result: dict) -> dict:
        """Another task that depends on the first"""
        print(f"Received: {upstream_result}")
        return {"final": "done"}
    
    # Define task dependencies
    result = my_task()
    final = another_task(result)
```

2. **Refresh Airflow UI** - DAG will appear automatically 

3. **Test the DAG:**
   - Go to http://localhost:8080
   - Find your DAG in the list
   - Click "Trigger DAG" 
   - Provide required parameters

### Editing Existing DAGs

**Adding a new task:**
```python
@task.python()
def new_task(file: dict, **context) -> dict:
    repository_id = context["params"]["repository_id"]
    # Task logic
    return {"processed": True}

# Add to workflow
new_results = new_task.expand(file=some_files)
```

**Modifying task parameters:**
```python
@task.python(
    retries=3,                           # Retry failed tasks 3 times
    retry_delay=timedelta(minutes=5),    # Wait 5 minutes between retries
    execution_timeout=timedelta(hours=2) # Task timeout
)
def long_running_task():
    # Task logic
    pass
```

**Adding new parameters:**
```python
params={
    "repository_id": Param(type="string", description="Repository ID"),
    "process_copybooks": Param(
        type="boolean", 
        default=True, 
        description="Whether to process copybook files"
    ),
}
```

3. **Changes are picked up automatically** - no restart needed

### DAG Best Practices

#### Task Function Structure
```python
@task.python()
def task_name(input_data: dict, **context) -> dict:
    """Clear description of what this task does"""
    
    # Get parameters
    repository_id = context["params"]["repository_id"]
    
    # Error handling
    try:
        # Task logic here
        result = process_data(input_data)
        return {"status": "success", "data": result}
    except Exception as e:
        logger.error(f"Task failed: {str(e)}")
        raise
```

#### Parallel Processing
```python
# Filter data for parallel processing
@task.python()
def filter_files(files: list[dict], file_type: str) -> list[dict]:
    return [f for f in files if f["type"] == file_type]

# Process in parallel using expand
files = get_all_files()
cobol_files = filter_files(files, "COBOL")
results = process_cobol.expand(file=cobol_files)
```

You can config the number of Celery workers in the `.env` file by changing `AIRFLOW__CELERY__WORKER_CONCURRENCY` (default is 16)

#### Task Dependencies
```python
# Sequential
task_a >> task_b >> task_c

# Parallel then join
[task_a, task_b] >> task_c

# Conditional execution
@task.python(trigger_rule=TriggerRule.ALL_DONE)
def cleanup_task():
    # Runs regardless of upstream success/failure
    pass
```

## Triggering DAGs

### Via Airflow UI
1. Go to http://localhost:8080
2. Find your DAG in the list
3. Click the "Play" button or "Trigger DAG"
4. Provide parameters in the dialog
5. Click "Trigger"

### Via API (with authentication)
**You need to convert the username and password to base64 and use it in the Authorization header.**
```bash
# Get authentication token first (via UI: Admin > Security > List Users > Generate Token)

# Trigger DAG with parameters
curl -X POST \
  "http://localhost:8080/api/v1/dags/<dag_id>/dagRuns" \
  -H "Authorization: Basic Base64(username:password)" \
  -H "Content-Type: application/json" \
  -d '{
    "conf": {
      "repository_id": "repo_123"
    }
  }'
```

### Via CLI (inside container)
```bash
# Execute inside scheduler container
docker exec -it mainframe-workers-airflow-scheduler-1 \
  airflow dags trigger reverse_repo \
  --conf '{"repository_id": "repo_123"}'

# List all DAGs
docker exec -it mainframe-workers-airflow-scheduler-1 \
  airflow dags list

# Test a specific task
docker exec -it mainframe-workers-airflow-scheduler-1 \
  airflow tasks test reverse_repo get_files 2024-01-01
```

## Monitoring and Debugging

### View Logs
1. **Via UI:** Click on task → View Logs
2. **Via CLI:** 
```bash
docker exec -it mainframe-workers-airflow-scheduler-1 \
  airflow tasks logs reverse_repo parse_cobol 2024-01-01 1
```

### Common Issues

**DAG not appearing:**
- Check for Python syntax errors
- Ensure `sys.path.append("./src")` is present
- Check Airflow logs: `docker logs mainframe-workers-airflow-scheduler-1`

**Import errors:**
- Verify all required modules are in `src/` directory
- Check that Docker volume mounts are correct
- Ensure custom packages are in `requirements.txt`

**Task failures:**
- Check task logs in UI
- Verify input parameters
- Test task logic independently

### Development Workflow

1. **Make changes to DAG file**
2. **Check DAG parsing:** Look for errors in Airflow UI
3. **Test with minimal data:** Use small parameter sets
4. **Monitor execution:** Watch task progress in Graph View
5. **Check logs:** Review task logs for issues
6. **Iterate:** Make adjustments and re-test

## Environment Configuration

### Required Files
- `docker-compose-airflow.yaml` - Airflow services configuration
- `Dockerfile.pyrequire_airflow` - Custom Airflow image with dependencies
- `requirements.txt` - Python packages (excluding apache-airflow)
- `.env` - Environment variables

### Environment Variables
```env
# .env file
AIRFLOW_UID=50000
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow
```

### Custom Dependencies
Add Python packages to `requirements.txt` (do NOT include `apache-airflow`):
```
antlr4-python3-runtime==4.13.2
azure-storage-blob==12.25.1
pandas==2.2.3
# ... other packages
```

## Customizing Docker Compose Airflow Setup

### Modifying Dockerfile.pyrequire_airflow

The `Dockerfile.pyrequire_airflow` file defines the custom Airflow image. You can modify it to install additional system packages, set environment variables, or customize the Python environment.

#### Current Dockerfile Structure
**Based** on Airflow version **2.10.5**:
```dockerfile
FROM apache/airflow:2.10.5

USER root

# Install Java 17 and clean up in a single layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/
RUN export JAVA_HOME

# Switch back to airflow user
USER ${AIRFLOW_UID:-50000}

# Copy and install Python requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --user -r /tmp/requirements.txt
```

#### Common Customizations

**1. Install Additional System Packages:**
```dockerfile
# Add after the Java installation
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    curl \
    wget \
    git \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

**2. Install Different Java Version:**
```dockerfile
# For Java 11 instead of Java 17
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-11-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
```

**3. Add Custom Environment Variables:**
```dockerfile
# Add before switching to airflow user
ENV CUSTOM_VAR=value
ENV PYTHONPATH=/opt/airflow/src:$PYTHONPATH
ENV TZ=UTC
```

**4. Install from Private Package Repository:**
```dockerfile
# Add authentication for private repos
COPY .netrc /root/.netrc
RUN chmod 600 /root/.netrc

# Install private packages
RUN pip install --no-cache-dir --user \
    --extra-index-url https://private-repo.com/simple \
    private-package==1.0.0
```

**5. Copy Custom Configuration Files:**
```dockerfile
# Copy custom configuration files
COPY config/custom-airflow.cfg /opt/airflow/airflow.cfg
COPY config/logging_config.py /opt/airflow/config/
```

**6. Install System Dependencies for Specific Packages:**
```dockerfile
# For packages that need compilation
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

#### Rebuild After Changes

After modifying the Dockerfile, rebuild the image:

```bash
# Rebuild with no cache to ensure fresh build
docker compose -f docker-compose-airflow.yaml build --no-cache

# Or rebuild and start
docker compose -f docker-compose-airflow.yaml up --build
```

#### Docker Compose Configuration

The `docker-compose-airflow.yaml` file references the custom Dockerfile:

```yaml
x-airflow-common:
  &airflow-common
  build: 
    context: .
    dockerfile: Dockerfile.pyrequire_airflow  # Custom Dockerfile
  env_file:
    - .env
```

For more information:
- [Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/2.10.5/index.html)
- [Airflow Task API](https://airflow.apache.org/docs/apache-airflow/2.10.5/core-concepts/taskflow.html)