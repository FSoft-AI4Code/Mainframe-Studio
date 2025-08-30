import os
import sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_core.messages.ai import AIMessage
from langchain_core.messages.tool import ToolMessage

from app.agents.graph import graph
from app.agents.utilities import print_event

# Let's create an example conversation a user might have with the assistant
tutorial_questions = [
    "Hi there, what can I do here?",
    "which jcl calls program CBACT01C",
]

# Update with the backup file so we can restart from the original place in each section
# db = update_dates(db)
thread_id = str(uuid.uuid4())

config = {
    "configurable": {
        "thread_id": thread_id,
        "repository_id": "1234567890",
        "is_assessed": True,
        "is_reversed": True,
    }
}

from IPython.display import Image, display

try:
    graph_image = graph.get_graph(xray=True).draw_mermaid_png()
    with open("graph.png", "wb") as f:
        f.write(graph_image)
    display(Image("graph.png"))
except Exception:
    # This requires some extra dependencies and is optional
    pass


_printed = set()
for question in tutorial_questions:
    events = graph.stream(
        {"messages": ("user", question)}, config, stream_mode="values"
    )
    for event in events:
        messages = event.get("messages")
        if isinstance(messages[-1], AIMessage) or isinstance(messages[-1], ToolMessage):
            print(messages[-1].content)
