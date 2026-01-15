
from pathlib import Path

download_path = Path.home() / "Downloads"
# 1. הגדרות וכללים
rules = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".wma", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".com"]
}

def sort_files(path_to_sort:Path):
    print(f"we going to order {path_to_sort}")        
    iter_downloads_folder = path_to_sort.iterdir()
    for path in iter_downloads_folder:
        if path.is_file():
            catagory_found = None
            file_ext = path.suffix.lower()
            for catagory, exts in rules.items():
                if file_ext in exts:
                    catagory_found = catagory
                    break
            # רשימת סיומות של קבצים בתהליך הורדה - נדלג עליהם
            if file_ext in [".crdownload", ".tmp", ".part", ".download"]:
                print(f"⏳ Skipping temporary file: {path.name}")
                continue
            if catagory_found:
                destination_dir =  path_to_sort / catagory_found
                print(f"{file_ext} belongs to {catagory_found} catagory")
            else: 
                destination_dir = path_to_sort / "unfamilier"

            destination_dir.mkdir(exist_ok= True)
            final_path = destination_dir / path.name   
            counter = 1
            while final_path.exists():
                # יצירת שם חדש: "שם_הקובץ_1.סיומת"
                new_name = f"{path.stem}_{counter}{path.suffix}"
                final_path = destination_dir / new_name
#                 counter += 1            
                
            path.rename(final_path)
            print(f"{path.name} moved to {destination_dir.name} folder")


sort_files(download_path)

    