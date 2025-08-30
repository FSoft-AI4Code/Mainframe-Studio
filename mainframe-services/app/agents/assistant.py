from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig

from app.agents.state import State
from app.agents.tools import query_relation_legacy_system, query_variable_possible_value
from app.config.llm_client import get_llm
from app.config.settings import get_settings

settings = get_settings()


class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        while True:
            configuration = config.get("configurable", {})
            repository_id = configuration.get("repository_id")
            is_assessed = configuration.get("is_assessed")
            is_reversed = configuration.get("is_reversed")
            state = {
                **state,
                "repository_id": repository_id,
                "is_assessed": is_assessed,
                "is_reversed": is_reversed,
            }
            result = self.runnable.invoke(state)

            if not result.tool_calls and (
                not result.content
                or isinstance(result.content, list)
                and not result.content[0].get("text")
            ):
                messages = state["messages"] + [("user", "Respond with a real output.")]
                state = {**state, "messages": messages}
            else:
                break
        return {"messages": result}


# Create a runnable for the assistant class.
llm = get_llm(model_type="assistant")

primary_assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a very careful and detail-oriented assistant specializing in legacy system migration projects. "
            "Your role is to:\n"
            "1. Analyze relationships and dependencies between files in legacy systems\n"
            "2. Provide general knowledge about legacy systems and migration processes\n"
            "3. Answer questions about source code and repository structure\n\n"
            "You have access to a graph querying tool to analyze file relationships and source code. You should:\n"
            "1. Help users formulate questions about system relationships, dependencies, and source code\n"
            "2. Always use the query_relation_legacy_system tool to retrieve information about the repository\n"
            "3. Provide clear explanations of the relationships and code structures found\n\n"
            "Important Guidelines:\n"
            "- For any question about file relationships, source code, or repository structure, use the query_relation_legacy_system tool\n"
            "- Base responses strictly on the data retrieved from the query_relation_legacy_system tool\n"
            "- For general legacy system knowledge, use your built-in knowledge\n"
            "- If a query is outside your scope, politely explain you can only help with:\n"
            "  a) File relationships and dependencies\n"
            "  b) Source code and repository structure\n"
            "  c) General legacy system/migration knowledge\n"
            "- Ask for clarification if a query is unclear\n\n"
            "Remember: Always use the query_relation_legacy_system tool for questions about the specific repository, "
            "source code, or file relationships. For general knowledge, use your built-in information.\n\n"
            "Current time: {time}.",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

assistant_tools = [query_relation_legacy_system, query_variable_possible_value]

assistant_runnable = primary_assistant_prompt | llm.bind_tools(assistant_tools)
