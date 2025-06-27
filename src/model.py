def classify_log(message):
    message = message.lower()
    if "cpu" in message:
        return "CPU"
    elif "memory" in message:
        return "Memory"
    elif "unauthorized" in message or "login" in message:
        return "Auth"
    elif "database" in message or "db" in message:
        return "Database"
    elif "crash" in message or "segmentation fault" in message:
        return "Crash"
    else:
        return "Other"
