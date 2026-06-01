from app.executors.collaboration_executor import (
    execute_collaboration
)

result = (
    execute_collaboration(
        "Plan my business trip to Delhi"
    )
)

print(result)