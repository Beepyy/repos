from sqlalchemy import select
from database import TaskORM, new_session
from shemas import STask,STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls,data:STaskAdd) -> int:
        async with new_session() as session:
            tast_dick=data.model_dump()

            task = TaskORM(**tast_dick)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_shemas = [STask.model_validate(task_model) for task_model in  task_models]
            return task_shemas