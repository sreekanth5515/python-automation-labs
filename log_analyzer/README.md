## Log Workflow

1. `generate_logs.py` is used to generate a large, realistic sample log file.
2. `sample.log` simulates production-style application and infrastructure logs.
3. `analyze_logs.py` processes the log file to:
   - count errors and warnings
   - aggregate errors by service
   - print timestamped log entries for quick triage

This setup mimics a simple incident investigation workflow.
