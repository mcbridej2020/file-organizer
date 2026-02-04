import os
import shutil
import logging 
from pathlib import Path

# --- Logging setup ---
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s | %(levelname)s | %(message)s",
	handlers=[
		logging.FileHandler(LOG_FILE),
		logging.StreamHandler()
	]
)

logger = logging.getLogger("file_organizer")
logger.info("File organizer started")

DOWNLOADS = "/mnt/c/Users/mcbrd/Downloads"

FILE_TYPES = {
	".pdf": "PDFs",
	".jpg": "Images",
	".jpeg": "Images",
	".png": "Images",
	".mp4": "Videos",
	".mov": "Videos",
}

DOWNLOADS = "/mnt/c/Users/mcbrd/Downloads"

FILE_TYPES = {
	".pdf": "PDFs",
	".jpg": "Images",
	".jpeg": "Images",
	".png": "Images",
	".mp4": "Videos",
	".mov": "Videos",
}

DRY_RUN = False  # set True to test safely

for filename in os.listdir(DOWNLOADS):
	source_path = os.path.join(DOWNLOADS, filename)

	# skip folders
	if os.path.isdir(source_path):
		continue

	for ext, folder in FILE_TYPES.items():
		if filename.lower().endswith(ext):
			destination_dir = os.path.join(DOWNLOADS, folder)
			destination_path = os.path.join(destination_dir, filename)

			# make sure destination folder exists
			os.makedirs(destination_dir, exist_ok=True)

			if DRY_RUN:
				logger.info(f"[DRY RUN] Would move: {filename} -> {folder}")
			else:
				try:
					shutil.move(source_path, destination_path)
					logger.info(f"Moved: {filename} -> {folder}")
				except Exception as e:
					logger.error(f"Failed to move {filename}: {e}")