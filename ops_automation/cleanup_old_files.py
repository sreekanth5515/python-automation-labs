import os
import time

# directory to clean
TARGET_DIR = "/tmp/cleanup_test"
DAYS_OLD = 7

now = time.time()
cutoff = now - (DAYS_OLD * 24 * 60 * 60)

if not os.path.exists(TARGET_DIR):
    print(f"Directory does not exist: {TARGET_DIR}")
    exit(1)

deleted_files = 0

for root, dirs, files in os.walk(TARGET_DIR):
    for name in files:
        file_path = os.path.join(root, name)
        file_mtime = os.path.getmtime(file_path)

        if file_mtime < cutoff:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
            deleted_files += 1

print(f"\nCleanup complete. Files deleted: {deleted_files}")
