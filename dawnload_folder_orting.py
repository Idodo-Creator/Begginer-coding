import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 1. הגדרות וכללים
rules = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".wma", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".com"]
}

download_path = Path.home() / "Downloads"

# 2. לוגיקת המיון לקובץ בודד
def sort_single_file(file_path: Path):
    if not file_path.is_file():
        return

    file_ext = file_path.suffix.lower()
    
    # התעלמות מקבצים זמניים של הורדות
    if file_ext in [".crdownload", ".tmp", ".part"]:
        return

    catagory_found = None
    for catagory, exts in rules.items():
        if file_ext in exts:
            catagory_found = catagory
            break

    destination_dir = download_path / (catagory_found if catagory_found else "unfamilier")
    destination_dir.mkdir(exist_ok=True)
    
    final_path = destination_dir / file_path.name
    counter = 1
    while final_path.exists():
        final_path = destination_dir / f"{file_path.stem}_{counter}{file_path.suffix}"
        counter += 1

    try:
        # השהיה קלה כדי לוודא שהקובץ לא נעול על ידי מערכת ההפעלה
        time.sleep(0.5)
        file_path.rename(final_path)
        print(f"✅ Moved: {file_path.name} -> {destination_dir.name}")
    except PermissionError:
        print(f"⚠️ Could not move {file_path.name} (File is in use)")

# 3. ה-Handler שמקשיב לאירועים
class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            sort_single_file(Path(event.src_path))

# 4. הגדרת ה-Observer והפעלתו
if __name__ == "__main__":
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, str(download_path), recursive=False)
    
    print(f"🚀 Monitoring started on: {download_path}")
    observer.start()
    
    try:
        while True:
            time.sleep(1) # שומר על התוכנית רצה
    except KeyboardInterrupt:
        observer.stop()
        print("\n👋 Monitoring stopped.")
    
    observer.join()

# def sort_files(path_to_sort:Path):
#     print(f"we going to order {path_to_sort}")        
#     iter_downloads_folder = path_to_sort.iterdir()
#     for path in iter_downloads_folder:
#         if path.is_file():
#             catagory_found = None
#             file_ext = path.suffix.lower()
#             for catagory, exts in rules.items():
#                 if file_ext in exts:
#                     catagory_found = catagory
#                     break

#             if catagory_found:
#                 destination_dir =  path_to_sort / catagory_found
#                 print(f"{file_ext} belongs to {catagory_found} catagory")
#             else: 
#                 destination_dir = path_to_sort / "unfamilier"

#             destination_dir.mkdir(exist_ok= True)
#             final_path = destination_dir / path.name   
#             counter = 1
#             while final_path.exists():
#                 # יצירת שם חדש: "שם_הקובץ_1.סיומת"
#                 new_name = f"{path.stem}_{counter}{path.suffix}"
#                 final_path = destination_dir / new_name
# #                 counter += 1            
                
#             path.rename(final_path)
#             print(f"{path.name} moved to {destination_dir.name} folder")
            
