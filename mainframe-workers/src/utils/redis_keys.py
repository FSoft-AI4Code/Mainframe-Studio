"""
Utility functions for generating Redis key names consistently across the application.
This helps avoid hardcoded key names in multiple places.
"""


def get_coordinator_pending_jobs_key(coordinator_id: str) -> str:
    """
    Get the Redis key for storing pending jobs for a coordinator.
    
    Args:
        coordinator_id: The unique identifier for the job coordinator
        
    Returns:
        str: Redis key for pending jobs
    """
    return f"coordinator:{coordinator_id}:pending_jobs"


def get_coordinator_next_task_key(coordinator_id: str) -> str:
    """
    Get the Redis key for storing next task configuration for a coordinator.
    
    Args:
        coordinator_id: The unique identifier for the job coordinator
        
    Returns:
        str: Redis key for next task configuration
    """
    return f"coordinator:{coordinator_id}:next_task"