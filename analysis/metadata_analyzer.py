from PIL import Image
import hashlib
import os

class MetadataAnalyzer:
    def extract_mac_times(self, file_path):
        stat = os.stat(file_path)
        return {
            'modified': stat.st_mtime,
            'accessed': stat.st_atime,
            'created': stat.st_ctime
        }

    def extract_exif(self, image_path):
        try:
            img = Image.open(image_path)
            return img._getexif()
        except Exception:
            return None

    def calculate_hash(self, file_path):
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
