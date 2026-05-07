"""
Celery application configuration.
Uses Redis as both broker and result backend.
"""

import os

from celery import Celery

# Load Redis URL from environment or default
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "Frank_worker",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["worker.tasks"],
)

# Celery configuration
celery_app.conf.update(
    # Serialization
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",

    # Timezone
    timezone="America/Sao_Paulo",
    enable_utc=True,

    # Task execution
    task_track_started=True,
    task_time_limit=900,        # Hard limit: 15 minutes
    task_soft_time_limit=600,   # Soft limit: 10 minutes (raises SoftTimeLimitExceeded)
    task_acks_late=True,        # Acknowledge after task completes (safer for crashes)

    # Worker
    worker_prefetch_multiplier=1,   # One task at a time per worker (renders are heavy)
    worker_max_tasks_per_child=5,   # Restart worker after 5 tasks (prevent memory leaks)
    worker_concurrency=1,           # One render at a time per worker

    # Result
    result_expires=86400,  # Results expire after 24 hours

    # Retry
    task_default_retry_delay=30,
    task_max_retries=2,
)
