import textwrap
import uuid

from loguru import logger

from config.llm_client import get_llm
from schema.java_migration import JavaCopybookStructure, JavaCopybookMigration, JavaBMSStructure, JavaBMSMigration
from schema.summarization import MigrationModel

BASE_PACKAGE = "com.migration.cobol"


def build_prompt_for_copybook_and_cobol_migration(copybook_contents: list[str], cobol_usage: str) -> str:
    formatted_copybooks = "\n\n".join(
        f"--- COPYBOOK {i+1} ---\n{content}" for i, content in enumerate(copybook_contents)
    )

    return textwrap.dedent(f"""
        You are a senior software engineer specialized in migrating COBOL CICS BMS applications to a modern Java Spring Boot 3 MVC architecture, targeting Java 17 best practices.

        You are tasked to migrate a **group of COPYBOOKs** that access/use/integrate with the same model,
        along with their usage inside a **COBOL program**, into appropriate Java components.

        Project structure:
        ```
        src/main/java/{BASE_PACKAGE.replace('.', '/')}/
            ├── controller/
            ├── dto/
            ├── model/
            ├── repository/
            ├── service/
            ├── view/
        src/main/resources/
            ├── application.properties
            ├── db/changelog/
                ├── "timestamp_table_name_create.yml
                └── db.changelog-master.yaml
        ```

        Java base package constant: `{BASE_PACKAGE}`

        **Input**:

        1. Group of COPYBOOKs:
        ```
        {formatted_copybooks}
        ```

        2. COBOL Usage Context:
        ```
        {cobol_usage}
        ```

        **Your task:**

        - Analyze the COPYBOOKs and COBOL usage.
        - Extract the **main table name** based on COBOL processing and COPYBOOK structure.
        - Use current UTC timestamp to generate the Liquibase changelog filename following the format: "timestamp_table_name_create.yml` where timestamp is formatted as `yyyyMMddHHmmss`.
        - Generate Java components and Liquibase changelog accordingly.

        **Output**: Return 
        - A **JSON array of objects**, each object must have:
            - `"file_name"`: relative file path (example: `model/DateInfo.java`, `repository/DateInfoRepository.java`, `db/changelog/20240428100500_date_info_create.yml`)
            - `"content"`: actual Java/YAML code inside the file.
        - A **JSON array of objects**, each object must have:
            - the main API endpoint this controller will expose (example: `/date-info`, `/roll-detail`).
            - The method of the API in Literal["GET", "POST", "PUT", "DELETE", "OPTIONS", "TRACE"]

        Example output:
        ```
        [
          {{
            "file_name": "model/DateInfo.java",
            "content": "package {BASE_PACKAGE}.model;\\n\\nimport lombok.*;\\n..."
          }},
          {{
            "file_name": "repository/DateInfoRepository.java",
            "content": "package {BASE_PACKAGE}.repository;\\n\\nimport {BASE_PACKAGE}.model.*;\\n..."
          }},
          {{
            "file_name": "controller/DateInfoController.java",
            "content": "package {BASE_PACKAGE}.controller;\\n\\nimport {BASE_PACKAGE}.service.*;\\n..."
          }},
          {{
            "file_name": "db/changelog/20240428100500_date_info_create.yml",
            "content": "databaseChangeLog:\\n  - changeSet:..."
          }},
          ...
        ],
        [
            {{
              "api_path": "/date-info",
              "api_method": "GET"
            }},
            {{
              "api_path": "/date-info",
              "api_method": "POST"
            }}
        ]
        ```

        **Guidelines**:

        - Use camelCase naming conventions for Java fields.
        - Mapping of COBOL types:
            - PIC X(n) → String
            - PIC 9(n) → Integer or Long
            - COMP-3 → BigDecimal
            - COMP → Integer
            - Dates → LocalDate or LocalDateTime
        - Java Classes:
            - Use Lombok: @Getter, @Setter, @Builder, @AllArgsConstructor, @NoArgsConstructor.
            - JPA Entities use jakarta.persistence annotations.
            - DTO classes should NOT have JPA annotations.
            - Controllers must expose REST APIs using @RestController, and must have a clear @RequestMapping base path.
            - Repositories extend JpaRepository<Model, IdType>.
            - Services implement the core business logic based on the COBOL flow.
        - Liquibase Changelog (YAML):
            - Always name the file as "timestamp_table_name_create.yml"
            - Correct syntax: databaseChangeLog, changeSet, createTable, columns, primaryKey.
            - Table and columns must match the model/entity fields.
        - API Migrate Output:
            - `api_path` must be simple, lowercase, plural if the entity is pluralizable (ex: `/dates`, `/roll-details`, etc.)
            - api_method: Literal["GET", "POST", "PUT", "DELETE", "OPTIONS", "TRACE"]
            - description: The purpose of this API
            - the api_method and api_path must be followed up the output and mapping with of the Controller

        **Important:**
        - If no database operation is detected, you can skip generating repository and liquibase file.
        - If the file is not a controller, you can omit `"api_path"`.
        - Always properly import other Java components based on `{BASE_PACKAGE}`.
        - Respond **only with the JSON array** of file objects. No extra text.
    """)


async def generate_java_components_from_cobol_summary(copybook_contents: list[str],
                                                      cobol_code: str) -> JavaCopybookStructure:
    try:
        prompt = build_prompt_for_copybook_and_cobol_migration(copybook_contents, cobol_code)
        llm = get_llm(model_type="assistant")
        structured_llm = llm.with_structured_output(JavaCopybookStructure)
        output = await structured_llm.ainvoke(prompt)

        logger.success("Java MVC code generated from COBOL summary")
        return output
    except Exception as e:
        logger.error(f"Failed to generate Java MVC: {e}")
        raise



@logger.catch
async def cobol_java_migration_summary(path: str,
                                       repository_id: str,
                                       cobol_file_name: str,
                                       copybook_contents: list[str],
                                       cobol_content: str) -> JavaCopybookMigration:
    """
    Process a single COBOL screen map asynchronously and return a structured MongoDB-compatible document.
    """
    try:
        result = await generate_java_components_from_cobol_summary(copybook_contents, cobol_content)
        logger.info("================== COBOL MIGRATION SUMMARY =================")
        logger.debug(result)
        logger.success("Java MVC code generated from COBOL summary")
        return JavaCopybookMigration(
            _id=uuid.uuid4().hex,
            repository_id=repository_id,
            status="done",
            path=path,
            linked_cobol=cobol_file_name,
            model_java=result.model_java,
            dto_java=result.dto_java,
            service_java=result.service_java,
            repository_java=result.repository_java,
            controller_java=result.controller_java,
            api_java=result.api_java,
            liquibase_java=result.liquibase_java,
        )

    except Exception as e:
        logger.error(f"Error migration COBOL screen: {e}")
        return JavaCopybookMigration(
            _id=uuid.uuid4().hex,
            repository_id=repository_id,
            status="fail",
            path=path,
            linked_cobol=cobol_file_name,
            model_java=None,
            dto_java=None,
            controller_java=None,
            repository_java=None,
            service_java=None,
            api_java=None,
            liquibase_java=None,
        )


def build_llm_prompt_for_bms_migration(
        bms_content: str,
        cobol_content: str,
        model_name: str,
        cobol_summary: MigrationModel
) -> str:
    """
    Build LLM prompt to migrate BMS file into modern Java MVC View Layer (HTML/Thymeleaf + View Controller).
    """
    api_path_formatted = ""
    if cobol_summary.get("apis"):
        api_path_formatted = "\n".join(
            [f"- {api["method"] or 'GET'} {api["path"] or '/unknown'}" for api in cobol_summary.get("apis")]
        )

    prompt = f"""You are a senior software engineer specialized in legacy modernization.

Your task:
- Migrate the given BMS screen definition and its usage in COBOL into a modern Java MVC View (HTML/Thymeleaf).
- Additionally, generate a Spring Boot Controller to map the screen to a GET endpoint.
- Map screen fields to appropriate DTO fields using the model name `{model_name}`.
- Bind screen actions (submit buttons, navigation) to corresponding API paths.

Inputs:

1. BMS Screen (Mapset Content) in html:
```bms
{bms_content}
```

2. COBOL Program using this screen:
```cobol
{cobol_content}
```

3. Available API paths:
{api_path_formatted if api_path_formatted else "- (none provided)"}

4. Java base package:
{BASE_PACKAGE}

Expected Output:
Respond with a single JSON object with the following fields:
{{
  "view_name": "Name of the generated view (based on BMS screen name)",
  "view_java": {{
    "file_name": "View file name (e.g., account-update.html)",
    "content": "... Thymeleaf-compatible HTML content here ..."
  }},
  "controller_java": {{
    "file_name": "Controller file name (e.g., AccountUpdateViewController.java)",
    "content": "... Spring Boot controller class mapping GET path to the view ..."
  }},
  "mapping_apis": [
    {{
      "api_path": "/api/xxx",
      "method": "POST/GET",
      "description": "Button label or screen action that triggers the API"
    }},
    ...
  ]
}}

Guidelines:
- Use Thymeleaf syntax for binding (e.g., th:field, th:value).
- Design form elements (<input>, <select>, <textarea>) based on BMS field attributes (e.g., UNPROT = input).
- Use screen field names to generate DTO field mappings under model `{model_name}`.
- Map screen actions (e.g., F5=Save) to correct API path from COBOL summary.
- Preserve BMS screen layout as much as possible for the View.
- For buttons (Submit/Save/Exit), map them clearly to corresponding API methods.

Controller generation:
- Create a Controller class inside package `{BASE_PACKAGE}.controller.view`
- Use `@RestController` or `@Controller` as needed.
- Use `@GetMapping` to map the screen display path.
- Return `String` with the view name (without `.html` extension) to render the Thymeleaf template.
- Example: `@GetMapping("/account-update")` → return "account-update"

Important:
- Only output a single valid JSON object.
- No explanation text, only the structured output JSON."""
    return prompt


async def generate_java_components_from_bms_summary(bms_content: str,
                                                    cobol_code: str,
                                                    model_name: str,
                                                    cobol_summary) -> JavaBMSStructure:
    try:
        prompt = build_llm_prompt_for_bms_migration(bms_content, cobol_code, model_name, cobol_summary)
        llm = get_llm(model_type="assistant")
        structured_llm = llm.with_structured_output(JavaBMSStructure)
        output = await structured_llm.ainvoke(prompt)

        logger.success("Java MVC code generated from BMS summary")
        return output
    except Exception as e:
        logger.error(f"Failed to generate Java MVC: {e}")
        raise


@logger.catch
async def bms_java_migration_summary(path: str,
                                     repository_id: str,
                                     cobol_content: str,
                                     bms_content: str,
                                     model_name: str,
                                     cobol_summary) -> JavaBMSMigration:
    """
    Process a single COBOL screen map asynchronously and return a structured MongoDB-compatible document.
    """
    try:
        result = await generate_java_components_from_bms_summary(bms_content, cobol_content, model_name, cobol_summary)
        logger.info("================== BMS MIGRATION SUMMARY =================")
        logger.debug(result)
        logger.success("Java MVC code generated from BMS summary")
        return JavaBMSMigration(
            _id=uuid.uuid4().hex,
            repository_id=repository_id,
            status="done",
            path=path,
            view_java=result.view_java,
            controller_java=result.controller_java,
            mapping_apis=result.mapping_apis
        )

    except Exception as e:
        logger.error(f"Error migration BMS screen: {e}")
        raise e
