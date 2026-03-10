import sys
import os
from scanner import ConfigExposureScanner
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        return
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return
    scanner = ConfigExposureScanner(folder_path)
    log = scanner.scan_and_remediate()
    scanner.print_summary(log)
    scanner.log_to_file(log)
if __name__ == "__main__":
    main()