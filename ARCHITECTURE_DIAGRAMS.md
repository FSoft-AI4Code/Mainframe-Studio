# Mainframe Modernization Platform - Architecture Diagrams

This document contains Mermaid diagrams visualizing the architecture described in ARCHITECTURE.md and README.md.

## 1. High-Level System Architecture

```mermaid
graph TB
    subgraph "User Interface Layer"
        UI[React Frontend<br/>Port: 3000]
        UI --> |HTTP/WebSocket| API
    end
    
    subgraph "API & Services Layer"
        API[FastAPI Services<br/>Port: 8000]
        WS[WebSocket Manager]
        AUTH[Authentication Service]
        API --> AUTH
        API --> WS
    end
    
    subgraph "Processing Layer"
        AIRFLOW[Apache Airflow<br/>Port: 8080]
        WORKERS[Parser Workers]
        QUEUE[RabbitMQ<br/>Port: 15672]
        AIRFLOW --> WORKERS
        WORKERS --> QUEUE
        API --> QUEUE
    end
    
    subgraph "Data Storage Layer"
        MONGO[(MongoDB<br/>Primary Data)]
        REDIS[(Redis<br/>Cache & Queue)]
        NEBULA[(Nebula Graph<br/>Dependencies)]
        AZURE[Azure Blob Storage<br/>Files]
    end
    
    subgraph "External Services"
        OPENAI[Azure OpenAI<br/>AI Analysis]
        GIT[Git Repositories]
    end
    
    API --> MONGO
    API --> REDIS
    WORKERS --> MONGO
    WORKERS --> NEBULA
    WORKERS --> AZURE
    WORKERS --> OPENAI
    API --> GIT
    
    style UI fill:#e1f5fe
    style API fill:#f3e5f5
    style AIRFLOW fill:#fff3e0
    style MONGO fill:#e8f5e8
    style OPENAI fill:#fff8e1
```

## 2. Component Architecture Detail

```mermaid
graph LR
    subgraph "Frontend (mainframe_platform_frontend)"
        REACT[React 18.2.0]
        REDUX[Redux Toolkit]
        QUERY[React Query]
        ANTD[Ant Design 5.6.3]
        D3[D3.js Visualization]
        
        REACT --> REDUX
        REACT --> QUERY
        REACT --> ANTD
        REACT --> D3
    end
    
    subgraph "Services (mainframe-services)"
        FASTAPI[FastAPI 0.115.2]
        MOTOR[MongoDB Motor]
        SAQ[SAQ Task Queue]
        LANGCHAIN[LangChain]
        JWT[JWT Authentication]
        
        FASTAPI --> MOTOR
        FASTAPI --> SAQ
        FASTAPI --> LANGCHAIN
        FASTAPI --> JWT
    end
    
    subgraph "Workers (mainframe-workers)"
        AF[Airflow Orchestration]
        ANTLR[ANTLR4 Parsers]
        PIKA[RabbitMQ Pika]
        LC[LangChain AI]
        
        AF --> ANTLR
        AF --> PIKA
        AF --> LC
    end
    
    REACT -->|REST API| FASTAPI
    FASTAPI -->|Message Queue| AF
    
    style REACT fill:#61dafb
    style FASTAPI fill:#009688
    style AF fill:#017cee
```

## 3. Data Flow Architecture

```mermaid
flowchart TD
    START([User Upload]) --> UPLOAD[Frontend File Upload]
    UPLOAD --> API[Services API Endpoint]
    API --> BLOB[Store in Azure Blob]
    API --> QUEUE[Queue Parsing Task]
    
    QUEUE --> DISPATCH[Worker Dispatcher]
    DISPATCH --> PARSER{Parser Selection}
    
    PARSER -->|COBOL| COBOL_P[COBOL Parser<br/>ANTLR4]
    PARSER -->|JCL| JCL_P[JCL Parser<br/>ANTLR4]
    PARSER -->|BMS| BMS_P[BMS Parser<br/>ANTLR4]
    PARSER -->|Other| OTHER_P[Other Parsers<br/>ANTLR4]
    
    COBOL_P --> ANALYZE[AI Analysis]
    JCL_P --> ANALYZE
    BMS_P --> ANALYZE
    OTHER_P --> ANALYZE
    
    ANALYZE --> GRAPH[Build Dependency Graph]
    GRAPH --> NEBULA[(Store in Nebula)]
    ANALYZE --> MONGO[(Store Results in MongoDB)]
    
    NEBULA --> WS[WebSocket Notification]
    MONGO --> WS
    WS --> FRONTEND[Update Frontend Dashboard]
    
    style START fill:#4caf50
    style FRONTEND fill:#2196f3
    style ANALYZE fill:#ff9800
    style NEBULA fill:#9c27b0
    style MONGO fill:#4caf50
```

## 4. Parser Support Matrix

```mermaid
graph TB
    subgraph "COBOL Variants"
        IBM[IBM COBOL<br/>Cobol85.g4]
        UNISYS[Unisys COBOL<br/>CobolUnisys.g4]
        DNP[DNP COBOL<br/>DNP.g4]
        ISUZU[Isuzu COBOL<br/>CobolIsuzu.g4]
    end
    
    subgraph "Mainframe Languages"
        JCL[JCL<br/>IBM_JCL.g4]
        BMS[BMS<br/>BMS.g4]
        CLIST[CLIST<br/>Clist.g4]
        PANEL[Panel<br/>Panel.g4]
        WFL[WFL<br/>WFL.g4]
        LDLP[LDLP<br/>LDLP.g4]
    end
    
    subgraph "Supporting Formats"
        COPY[Copybooks<br/>CopyBook.g4]
        BATCH[Batch Scripts<br/>Batch.g4]
        OGL[OGL<br/>OGL.g4]
    end
    
    DISPATCHER[Parser Dispatcher] --> IBM
    DISPATCHER --> UNISYS
    DISPATCHER --> DNP
    DISPATCHER --> ISUZU
    DISPATCHER --> JCL
    DISPATCHER --> BMS
    DISPATCHER --> CLIST
    DISPATCHER --> PANEL
    DISPATCHER --> WFL
    DISPATCHER --> LDLP
    DISPATCHER --> COPY
    DISPATCHER --> BATCH
    DISPATCHER --> OGL
    
    style DISPATCHER fill:#ff6b6b
    style IBM fill:#4ecdc4
    style JCL fill:#45b7d1
    style COPY fill:#96ceb4
```

## 5. API Services Architecture

```mermaid
graph LR
    CLIENT[Client Applications] --> GATEWAY[API Gateway]
    
    GATEWAY --> AUTH[/auth<br/>Authentication]
    GATEWAY --> USERS[/users<br/>User Management]
    GATEWAY --> PROJECTS[/projects<br/>Project Lifecycle]
    GATEWAY --> REPOS[/repositories<br/>Repository Handling]
    GATEWAY --> ASSESS[/assessments<br/>Complexity Analysis]
    GATEWAY --> REVERSE[/reverse<br/>Reverse Engineering]
    GATEWAY --> CHAT[/chat<br/>AI Assistant]
    GATEWAY --> SUMMARY[/summarization<br/>Code Summary]
    GATEWAY --> MIGRATE[/migration<br/>Migration Tools]
    GATEWAY --> DEAD[/deadcode<br/>Dead Code Detection]
    GATEWAY --> DUP[/duplicate-files<br/>Duplicate Analysis]
    GATEWAY --> DATA[/datasets<br/>Dataset Management]
    GATEWAY --> UTIL[/utilities<br/>System Utilities]
    
    AUTH --> JWT[JWT Service]
    PROJECTS --> MONGO1[(MongoDB)]
    REPOS --> GIT[Git Integration]
    ASSESS --> AI1[AI Analysis]
    CHAT --> OPENAI[Azure OpenAI]
    
    style CLIENT fill:#e3f2fd
    style GATEWAY fill:#f3e5f5
    style CHAT fill:#fff3e0
    style OPENAI fill:#ffecb3
```

## 6. Message Queue Architecture

```mermaid
graph TB
    subgraph "Exchanges"
        PARSER_EX[parser_exchange]
        SUMM_EX[summarization_exchange]
        MIG_EX[migration_exchange]
        MOD_EX[modernization_exchange]
    end
    
    subgraph "Parser Queues"
        COBOL_Q[cobol_unisys_parser_queue]
        JCL_Q[jcl_parser_queue]
        BMS_Q[bms_parser_queue]
        COPY_Q[copybook_parser_queue]
    end
    
    subgraph "Analysis Queues"
        SUMM_Q[bms_summarization_queue]
        ASSESS_Q[assessment_queue]
        GRAPH_Q[graph_analysis_queue]
    end
    
    subgraph "Migration Queues"
        JAVA_Q[cobol_java_migration_queue]
        MOD_Q[bms_modernization_queue]
    end
    
    subgraph "Workers"
        PARSER_W[Parser Workers]
        SUMM_W[Summarization Workers]
        MIG_W[Migration Workers]
        GRAPH_W[Graph Workers]
    end
    
    PARSER_EX --> COBOL_Q
    PARSER_EX --> JCL_Q
    PARSER_EX --> BMS_Q
    PARSER_EX --> COPY_Q
    
    SUMM_EX --> SUMM_Q
    PARSER_EX --> ASSESS_Q
    PARSER_EX --> GRAPH_Q
    
    MIG_EX --> JAVA_Q
    MOD_EX --> MOD_Q
    
    COBOL_Q --> PARSER_W
    SUMM_Q --> SUMM_W
    JAVA_Q --> MIG_W
    GRAPH_Q --> GRAPH_W
    
    style PARSER_EX fill:#ffcdd2
    style SUMM_EX fill:#c8e6c9
    style MIG_EX fill:#dcedc8
    style MOD_EX fill:#f8bbd9
```

## 7. Data Storage Schema

```mermaid
erDiagram
    USERS {
        string _id
        string email
        string name
        array permissions
        datetime created_at
    }
    
    PROJECTS {
        string _id
        string name
        string description
        string owner_id
        array repository_ids
        object status
        datetime created_at
    }
    
    REPOSITORIES {
        string _id
        string project_id
        string name
        string git_url
        object parsing_status
        array supported_languages
    }
    
    ASSESSMENTS {
        string _id
        string project_id
        string repository_id
        object complexity_metrics
        object summary
        datetime assessed_at
    }
    
    PARSED_FILES {
        string _id
        string repository_id
        string file_path
        string file_type
        string parser_used
        object ast_data
        array dependencies
    }
    
    CHAT_SESSIONS {
        string _id
        string user_id
        string project_id
        array messages
        datetime created_at
    }
    
    USERS ||--o{ PROJECTS : owns
    PROJECTS ||--o{ REPOSITORIES : contains
    REPOSITORIES ||--o{ ASSESSMENTS : has
    REPOSITORIES ||--o{ PARSED_FILES : contains
    USERS ||--o{ CHAT_SESSIONS : participates
```

## 8. Security Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        BROWSER[Web Browser]
        MOBILE[Mobile App]
    end
    
    subgraph "Security Layer"
        TLS[TLS 1.3 Encryption]
        CORS[CORS Policy]
        RATE[Rate Limiting]
    end
    
    subgraph "Authentication"
        JWT_AUTH[JWT Authentication]
        REFRESH[Token Refresh]
        RBAC[Role-Based Access]
    end
    
    subgraph "API Protection"
        VALIDATE[Request Validation]
        SANITIZE[Input Sanitization]
        AUDIT[Audit Logging]
    end
    
    subgraph "Data Protection"
        DB_AUTH[Database Authentication]
        ENCRYPT[Data Encryption at Rest]
        ENV[Environment Variables]
    end
    
    BROWSER --> TLS
    MOBILE --> TLS
    TLS --> CORS
    CORS --> RATE
    RATE --> JWT_AUTH
    JWT_AUTH --> REFRESH
    JWT_AUTH --> RBAC
    RBAC --> VALIDATE
    VALIDATE --> SANITIZE
    SANITIZE --> AUDIT
    AUDIT --> DB_AUTH
    DB_AUTH --> ENCRYPT
    ENCRYPT --> ENV
    
    style TLS fill:#f44336
    style JWT_AUTH fill:#2196f3
    style ENCRYPT fill:#4caf50
    style RBAC fill:#ff9800
```

## 9. Deployment Architecture

```mermaid
graph TB
    subgraph "Development Environment"
        DEV_FE[Frontend Dev Server<br/>yarn start]
        DEV_API[FastAPI Dev<br/>uvicorn reload]
        DEV_WORK[Airflow Local<br/>make dev]
        DEV_DB[Local Databases<br/>Docker Compose]
    end
    
    subgraph "Production Environment"
        subgraph "Azure Container Instances"
            PROD_FE[Frontend Container<br/>Nginx + Static Files]
            PROD_API[Services Container<br/>FastAPI + Gunicorn]
            PROD_WORK[Workers Container<br/>Airflow + Celery]
        end
        
        subgraph "Managed Services"
            ATLAS[MongoDB Atlas]
            REDIS_AZURE[Azure Redis Cache]
            RABBITMQ_CLOUD[CloudAMQP]
            BLOB_STORAGE[Azure Blob Storage]
        end
    end
    
    subgraph "CI/CD Pipeline"
        GIT_REPO[Git Repository]
        JENKINS[Jenkins CI]
        DOCKER_BUILD[Docker Build]
        DEPLOY[Deploy to Azure]
    end
    
    GIT_REPO --> JENKINS
    JENKINS --> DOCKER_BUILD
    DOCKER_BUILD --> DEPLOY
    DEPLOY --> PROD_FE
    DEPLOY --> PROD_API
    DEPLOY --> PROD_WORK
    
    PROD_API --> ATLAS
    PROD_API --> REDIS_AZURE
    PROD_WORK --> RABBITMQ_CLOUD
    PROD_API --> BLOB_STORAGE
    
    style DEV_FE fill:#e1f5fe
    style PROD_FE fill:#1565c0
    style JENKINS fill:#dc7633
    style ATLAS fill:#27ae60
```

## 10. Processing Pipeline Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant A as API Service
    participant B as Azure Blob
    participant Q as RabbitMQ
    participant W as Worker
    participant P as Parser (ANTLR4)
    participant AI as Azure OpenAI
    participant N as Nebula Graph
    participant M as MongoDB
    participant WS as WebSocket
    
    U->>F: Upload Files
    F->>A: POST /repositories/upload
    A->>B: Store Files
    A->>Q: Queue Parsing Tasks
    A->>F: Upload Confirmed
    
    Q->>W: Dispatch Tasks
    W->>P: Parse Files
    P->>W: AST + Metadata
    W->>AI: Analyze Code
    AI->>W: Analysis Results
    
    W->>N: Store Dependencies
    W->>M: Store Results
    W->>WS: Notify Completion
    WS->>F: Real-time Update
    F->>U: Show Results
    
    Note over P: COBOL, JCL, BMS<br/>Grammar-based parsing
    Note over AI: Code summarization<br/>Complexity analysis
    Note over N: Dependency graphs<br/>Call relationships
```

## 11. Technology Stack Overview

```mermaid
mindmap
  root)Mainframe Platform(
    Frontend
      React 18.2
      TypeScript
      Redux Toolkit
      Ant Design 5.6
      D3.js Charts
      XYFlow React
    Backend
      FastAPI 0.115
      Python 3.10+
      MongoDB Motor
      JWT Auth
      SAQ Queue
      LangChain
    Workers  
      Apache Airflow
      Python 3.12+
      ANTLR4 Parsers
      RabbitMQ Pika
      Azure OpenAI
    Storage
      MongoDB
      Redis Cache
      Nebula Graph
      Azure Blob
    DevOps
      Docker
      Jenkins CI
      Poetry
      Yarn
      Helm Charts
```

## 12. User Journey Flow

```mermaid
journey
    title Mainframe Modernization User Journey
    section Project Setup
      Create Account: 5: User
      Login to Platform: 5: User
      Create New Project: 4: User
      Configure Settings: 3: User
    section Code Upload
      Upload Repository: 4: User
      Select File Types: 4: User
      Start Processing: 5: User
      Monitor Progress: 3: User
    section Analysis
      View Parsing Results: 5: User
      Explore Dependencies: 4: User
      Review Complexity: 4: User
      Chat with AI Assistant: 5: User
    section Modernization
      Generate Migration Plan: 5: User
      Review Recommendations: 4: User
      Export Documentation: 4: User
      Download Artifacts: 5: User
```

---

These Mermaid diagrams provide comprehensive visualization of your Mainframe Modernization Platform architecture, covering system components, data flows, deployment patterns, and user interactions. Each diagram can be rendered in any Mermaid-compatible viewer or documentation system.