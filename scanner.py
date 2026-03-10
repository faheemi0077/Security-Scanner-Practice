import os
import re
class ConfigExposureScanner:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.risky_patterns = [
            (r"0\.0\.0\.0", "127.0.0.1"),
            (r"0\.0\.0\.0/0", "127.0.0.1/32"),
            (r"\b(?!(10\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])))(\d{1,3}\.){3}\d{1,3}\b", "[REDACTED_PUBLIC_IP]")
        ]
    def scan_and_remediate(self):
        exposure_log = []
        for filename in os.listdir(self.folder_path):
            if not filename.endswith(('.env', '.json', '.yaml', '.yml')):
                continue
            file_path = os.path.join(self.folder_path, filename)
            with open(file_path, 'r') as file:
                content = file.read()
            original_content = content
            redacted = False
            for pattern, replacement in self.risky_patterns:
                new_content = re.sub(pattern, replacement, content)
                if new_content != content:
                    exposure_log.append(f"{filename}: Found pattern '{pattern}' → replaced.")
                    content = new_content
                    redacted = True
            if redacted:
                quarantined_path = os.path.join(self.folder_path, filename.replace('.', '_quarantined.'))
                with open(quarantined_path, 'w') as qf:
                    qf.write(content)
                exposure_log.append(f"Saved sanitized copy to: {quarantined_path}")
        return exposure_log
    def log_to_file(self, log_list, filename='remediation_log.txt'):
        log_path = os.path.join(self.folder_path, filename)
        with open(log_path, 'w') as f:
            for line in log_list:
                f.write(line + '\n')
    def print_summary(self, log_list):
        print("\n--- Exposure Scan Summary ---")
        for line in log_list:
            print(line)
        print("--- End of Report ---\n")
