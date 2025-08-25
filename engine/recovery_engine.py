import pytsk3
import os

class RecoveryEngine:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = pytsk3.Img_Info(image_path)
        self.fs = None
        self._open_filesystem()

    def _open_filesystem(self):
        # Try NTFS, then FAT32
        try:
            self.fs = pytsk3.FS_Info(self.img)
        except Exception as e:
            self.fs = None

    def scan_deleted_files(self):
        if not self.fs:
            return []
        deleted_files = []
        directory = self.fs.open_dir(path="/")
        for entry in directory:
            if not hasattr(entry, "info") or not entry.info.meta:
                continue
            meta = entry.info.meta
            if meta.flags & pytsk3.TSK_FS_META_FLAG_UNALLOC:
                deleted_files.append({
                    "name": entry.info.name.name.decode() if entry.info.name.name else "",
                    "size": meta.size,
                    "addr": meta.addr
                })
        return deleted_files

    def recover_file(self, file_metadata, output_dir):
        if not self.fs:
            return False
        try:
            file_obj = self.fs.open_meta(file_metadata["addr"])
            out_path = os.path.join(output_dir, file_metadata["name"])
            with open(out_path, "wb") as f:
                f.write(file_obj.read_random(0, file_metadata["size"]))
            return True
        except Exception:
            return False
