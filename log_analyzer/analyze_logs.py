log_file = "sample.log"

error_count = 0
warning_count = 0

error_logs = []
warning_logs = []

with open(log_file, "r") as file:
    for line in file:
        line = line.strip()

        if "ERROR" in line:
            error_count += 1
            error_logs.append(line)

        elif "WARNING" in line:
            warning_count += 1
            warning_logs.append(line)

print("Log Analysis Report")
print("-------------------")
print(f"Errors   : {error_count}")
print(f"Warnings : {warning_count}")

print("\nError Details:")
for log in error_logs:
    print(log)

print("\nWarning Details:")
for log in warning_logs:
    print(log)
