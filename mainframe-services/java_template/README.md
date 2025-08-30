# Spring Boot Demo Project

This is a Spring Boot application with PostgreSQL database integration.

## Prerequisites

- Docker and Docker Compose

## Project Structure

```
demo/
├── src/
│   ├── main/
│   │   ├── java/
│   │   └── resources/
│   └── test/
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## Database Configuration

The application uses PostgreSQL with the following configuration:
- Database: mainframe
- Username: admin
- Password: secret123
- Port: 5432

## Getting Started

### Using Docker (Recommended)

1. Build and start all services:
   ```bash
   docker-compose up --build
   ```

   This will:
   - Build the Spring Boot application
   - Start PostgreSQL database
   - Start the Spring Boot application
   - Set up the network between services

2. Access the application:
   - Web interface: http://localhost:8080
   - PostgreSQL: localhost:5432

### Development Setup (Optional)

If you want to run the application locally for development:

1. Start only the PostgreSQL database:
   ```bash
   docker-compose up postgres
   ```

2. Run the Spring Boot application using Maven:
   ```bash
   ./mvnw spring-boot:run
   ```

## Stopping the Application

1. Stop all services:
   ```bash
   docker-compose down
   ```

To remove all data and start fresh:
```bash
docker-compose down -v
```

## Development

The application uses:
- Spring Boot
- PostgreSQL
- Liquibase for database migrations
- Thymeleaf for templating

## Logging

The application is configured with the following logging levels:
- Root: INFO
- Hibernate SQL: DEBUG
- Liquibase: DEBUG

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 