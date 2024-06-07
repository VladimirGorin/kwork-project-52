import threading

def send():
    import subprocess
    subprocess.call(['python3', 'send.py'])

threads = []
for _ in range(10):
    thread = threading.Thread(target=send)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
