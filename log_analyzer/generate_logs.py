from datetime import datetime, timedelta
import random

services = [
    "auth-service",
    "payment-service",
    "order-service",
    "inventory-service",
    "network",
    "system-monitor",
    "kubernetes"
]

levels = ["INFO", "WARNING", "ERROR"]

messages = {
    "INFO": [
        "Request processed successfully",
        "Connection established",
        "Retry successful",
        "Health check passed",
        "Pod started",
        "Autoscaling event triggered",
        "User login successful",
        "Cache refreshed"
    ],
    "WARNING": [
        "Memory usage exceeded threshold",
        "Disk usage exceeded threshold",
        "Slow response detected",
        "High CPU utilization"
    ],
    "ERROR": [
        "Database connection timeout",
        "Authentication failed",
        "Service unavailable",
        "Connection reset by peer",
        "Failed after retries",
        "Pod crashed due to OOM"
    ]
}

start_time = datetime(2025, 12, 24, 9, 0, 0)

with open("sample.log", "w") as log:
    current_time = start_time

    for _ in range(2000):  # creates ~2000 log lines
        level = random.choices(
            levels, weights=[94, 5, 1], k=1
        )[0]

        service = random.choice(services)
        message = random.choice(messages[level])

        log_line = (
            f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"{level} [{service}] {message}\n"
        )

        log.write(log_line)
        current_time += timedelta(seconds=random.randint(1, 5))

print("sample.log generated successfully")
