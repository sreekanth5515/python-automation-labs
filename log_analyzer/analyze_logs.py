import sys

if len(sys.argv) < 2:
    print("Usage: python3 analyze_logs.py <log_file>")
    sys.exit(1)

log_file = sys.argv[1]


error_count = 0
warning_count = 0

error_logs = []
warning_logs = []
    
error_by_service = {}

with open(log_file, "r") as file:
    for line in file:
        line = line.strip()
#count the Errors and add them to append list
        if "ERROR" in line:
            error_count += 1
            error_logs.append(line)
# extract service name inside [ ]
            start = line.find("[")
            end = line.find("]")

            if start != -1 and end != -1:
                service = line[start + 1:end]
            else:
                service = "unknown"

            error_by_service[service] = error_by_service.get(service, 0) + 1

#count the Warnings and add them to append list
        elif "WARNING" in line:
            warning_count += 1
            warning_logs.append(line)
print("Log Analysis Report")
print("-------------------")
print(f"Errors   : {error_count}")
print(f"Warnings : {warning_count}")

print("\nErrors by Service:")
for service, count in sorted(error_by_service.items()):
    print(f"{service} : {count}")

print("\nError Details:")
for log in error_logs:
    print(log)

print("\nWarning Details:")
for log in warning_logs:
    print(log)