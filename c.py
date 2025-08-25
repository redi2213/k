import os
from datetime import datetime

EXCLUDE_FILES = {"Cache.maker.py"}  # فایل‌هایی که نباید داخل لیست بیان

def generate_cache_manifest(base_dir="."):
    cache_file = os.path.join(base_dir, "cache.manifest")

    with open(cache_file, "w", encoding="utf-8") as f:
        # Header
        f.write("CACHE MANIFEST\n")
        f.write(f"# Generated: {datetime.utcnow().isoformat()} UTC\n\n")
        
        # Cached files
        f.write("CACHE:\n")

        for root, _, files in os.walk(base_dir):
            for filename in files:
                if filename in EXCLUDE_FILES:
                    continue
                filepath = os.path.relpath(os.path.join(root, filename), base_dir)
                f.write(f"{filepath.replace(os.sep, '/')}\n")

        # Fallback (optional)
        f.write("\nFALLBACK:\n")

        # Network (optional)
        f.write("\nNETWORK:\n")
        f.write("*\n")

    print(f"✅ cache.manifest ساخته شد ({cache_file})")

if __name__ == "__main__":
    generate_cache_manifest()