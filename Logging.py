import uuid


class log_entry:
    def __init__(self, func, timestamp, error_type, row_count):
        self.id = str(uuid.uuid4())
        self.func = func
        self.timestamp = timestamp
        self.error_type = error_type
        self.row_count = row_count


class Logger:
    def __init__(self):
        self.log_list = []
    def add_log_entry(self, log_entry):
        self.log_list.append(log_entry)
    def upload_log_entries(self, type = "text"):
        ### Upload to text file or db or both
        if type == "text":
            return None
        return None



