import os
import shutil

DOWNLOADS = "/mnt/c/Users/mcbrd/Downloads"

FILE_TYPES = {
	".pdf": "PDFs",
	".jpg": "Images",
	".jpeg": "Images",
	".png": "Images",
	".mp4": "Videos",
	".mov": "Videos",
}

DRY_RUN = False # change to false when ready

for filename in os.listdir(DOWNLOADS):
	source_path = os.path.join(DOWNLOADS, filename)

	# skip folders
	if os.path.isdir(source_path):
		continue

	for ext, folder in FILE_TYPES.items():
		if filename.lower().endswith(ext):
			destination_path = os.path.join(DOWNLOADS, folder, filename)

			if DRY_RUN:
				print(f"[DRY RUN] Would move: {filename} -> {folder}")
			else:
				shutil.move(source_path, destination_path)
				print(f"Moved: {filename} -> {folder}")
