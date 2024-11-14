import os
from pathlib import Path
from typing import Generator

from google.cloud import storage

CHUNK_SIZE = 1 * 1024 * 1024  # 1 MB


def chunk_file(file_full_path: str) -> Generator[bytes, None, None]:
    file = Path(file_full_path)
    with file.open("rb") as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            yield chunk


if __name__ == "__main__":
    test_bucket_name = "test-bucket"
    filepath = "train.jsonl"
    blob_name = "train.jsonl"

    os.environ["STORAGE_EMULATOR_HOST"] = "http://gcs:9023"

    client = storage.Client()
    bucket = client.bucket(test_bucket_name)
    blob = bucket.blob(blob_name)

    with blob.open("wb", chunk_size=CHUNK_SIZE) as blob_writer:
        for piece in chunk_file(filepath):
            blob_writer.write(piece)

    for b in bucket.list_blobs():
        print(b.name)
