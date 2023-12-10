import subprocess
import datetime
import os
import sys
import time
import schedule

def run_robocopy(source, destination, log_file):
    robocopy_cmd = [
        "robocopy", source, destination, "/MIR", "/COPYALL", "/R:10", "/W:10", "/LOG+:" + log_file, "/NP", "/TEE"
    ]
    try:
        subprocess.run(robocopy_cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Robocopy failed with error: {e}")
        return False

def create_backup_folder(destination):
    today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(destination, "backup_" + today)
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    return backup_folder

def backup_procedure():
    source = input("Enter the source drive path (e.g., D:\\): ")
    destination = input("Enter the destination path for backup: ")
    
    if not os.path.exists(source):
        print("Source path does not exist. Exiting.")
        sys.exit(1)

    backup_folder = create_backup_folder(destination)
    log_file = os.path.join(backup_folder, "backup_log.txt")

    print(f"Starting backup from {source} to {backup_folder}")
    if not run_robocopy(source, backup_folder, log_file):
        print("Backup failed. Please check the log file for details.")
    else:
        print("Backup completed successfully.")

def schedule_backup(interval):
    schedule.every(interval).hours.do(backup_procedure)
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    interval = int(input("Enter backup interval in hours (e.g., 24 for daily backup): "))
    try:
        schedule_backup(interval)
    except ValueError:
        print("Invalid interval. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
