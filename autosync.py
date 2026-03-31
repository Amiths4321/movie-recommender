import subprocess, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GitAutoSync(FileSystemEventHandler):
    def on_modified(self, event):
        if '.git' in event.src_path:
            return
        print(f"Change detected: {event.src_path}")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "auto-sync"])
        subprocess.run(["git", "push"])

observer = Observer()
observer.schedule(GitAutoSync(), path='.', recursive=True)
observer.start()
print("Auto-sync running... Ctrl+C to stop")
try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()