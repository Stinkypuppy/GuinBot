import os
import subprocess
import threading
import time

# Function to start a tmate session and execute a command
def start_tmate_session(session_number):
    tmate_socket_path = f'/tmp/tmate-{session_number}.sock'
    
    # Start tmate session
    subprocess.Popen(['tmate', '-S', tmate_socket_path, 'new-session', '-d'], 
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
    time.sleep(2)  # Wait for tmate session to initialize

    # Send the command to the tmate session
    command = "cd /content/Guin*/data && python bot.py"
    subprocess.Popen(['tmate', '-S', tmate_socket_path, 'send-keys', command, 'C-m'], 
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)

    # Retrieve and display the HTTP web link
    web_link_process = subprocess.Popen(['tmate', '-S', tmate_socket_path, 'display', '-p', '#{tmate_web}'], 
                                        stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE)
    web_link = web_link_process.stdout.readline().decode().strip()
    print(f'Session {session_number}: {web_link}')

# Install tmate if not already installed
if not os.path.exists('/usr/bin/tmate'):
    os.system('apt-get update')
    os.system('apt-get install -y tmate')

# Start 10 tmate sessions in separate threads
threads = []
for i in range(10):
    thread = threading.Thread(target=start_tmate_session, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Keep the script running to maintain the sessions
print("All tmate sessions are running with the specified command. Keep this script running to maintain the sessions.")
while True:
    pass
