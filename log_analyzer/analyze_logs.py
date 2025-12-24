log_file = "sample.log"

error_count = 0
warning_count = 0

with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1

print("Log Analysis Report")
print("-------------------")
print(f"Errors   : {error_count}")
print(f"Warnings : {warning_count}")
