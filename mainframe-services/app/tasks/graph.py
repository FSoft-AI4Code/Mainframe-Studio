from app.config.database import get_database
from app.controllers.graph_controller import create_graph
from app.controllers.chat_controller import init_nebula


async def trigger_create_graph(ctx, *, repo_id):
    db = await get_database()
    await create_graph(db=db, repository_id=repo_id)


async def trigger_init_nebula(ctx, *, repo_id):
    db = await get_database()
    await init_nebula(db=db, repository_id=repo_id)
