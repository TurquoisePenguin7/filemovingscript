from pathlib import Path
import shutil


downloads_location = Path.home() / "Downloads"
file_extensions = ['mp4', 'webm', 'jpeg', 'jpg', 'png', 'pdf', '7z', 'bz2', 'gz', 'zip', 'gif', 'rar']
video_location = Path.home() / "Videos"
image_location = Path.home() / "Pictures"
pdf_location = Path.home() / "Documents" / 'pdfs'
zip_location = Path.home() / "Documents" / 'zips'

try:
    pdf_location.mkdir(exist_ok=False)
    zip_location.mkdir(exist_ok=False)
except FileExistsError as e:
    print(f"Directory {e} exists, skipping...")
    

for extension in file_extensions:
   for file in downloads_location.glob(f"*.{extension}"):
      match extension:
         case 'mp4' | 'webm':
            shutil.move(file, video_location)
         case 'png' | 'jpeg' | 'gif' | 'jpg':
            shutil.move(file, image_location)
         case 'pdf':
            shutil.move(file, pdf_location)
         case '7z' | 'bz2' | 'gz' | 'zip' | 'rar':
            shutil.move(file, zip_location)

print("Finished moving files.")
