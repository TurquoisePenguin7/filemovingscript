from pathlib import Path
import shutil


DOWNLOADS_LOCATION = Path.home() / "Downloads"
VIDEO_LOCATION = Path.home() / "Videos"
IMAGE_LOCATION = Path.home() / "Pictures"
PDF_LOCATION = Path.home() / "Documents" / 'pdfs'
ZIP_LOCATION = Path.home() / "Documents" / 'zips'


   
file_extensions = {
   'mp4': VIDEO_LOCATION,
   'webm': VIDEO_LOCATION,
   'jpeg': IMAGE_LOCATION,
   'jpg': IMAGE_LOCATION,
   'png': IMAGE_LOCATION,
   'pdf': PDF_LOCATION,
   '7z': ZIP_LOCATION,
   'bz2': ZIP_LOCATION,
   'gz': ZIP_LOCATION,
   'zip': ZIP_LOCATION,
   'gif': IMAGE_LOCATION,
   'xz': ZIP_LOCATION,

}

class CleaningFiles:

   def __init__(self):
      self._check_exists()
      self._check_file_formats()

   def _check_exists(self):

      """Checking if the Path exists, if not - creates one"""

      try:
         PDF_LOCATION.mkdir(exist_ok=False)
         ZIP_LOCATION.mkdir(exist_ok=False)
      except FileExistsError as e:
         print(f"Directory {e} exists, skipping folder creation...")
   
   def _check_file_formats(self):
      """Checking file formats, stripping their suffixes, checking them in the extensions dictionary, skip it if not in dictionary and moving them to the location.
         You can add your own extensions if needed.
      """

      for file in DOWNLOADS_LOCATION.glob("*"):
         file_suffix = str(file.suffix).strip('.')
         folder_location = file_extensions.get(file_suffix)
         if folder_location == None:
            continue
         shutil.move(file, folder_location)
         print(f"Moving {file} to {folder_location}")

if __name__ == "__main__":
   filecleaner = CleaningFiles()
