# Description 

This repository is to replicate an issue with [oittaa/gcp-storage-emulator](https://github.com/oittaa/gcp-storage-emulator)

Within the `Dockerfile`, it downloads a sample data with wget. 

In `main.py`, it will try to upload the sample data file by chunking.

I use `wait-for-it.sh` to see if the gcs emulator is ready. 

# How to execute? 
Tested on macOS 15.1.

```bash 
make run
```

# Expectation 
You will get. From the investigation, it seems pushing the first piece of chunk. 

```text
Traceback (most recent call last):
  File "/app/main.py", line 33, in <module>
    blob_writer.write(piece)
  File "/root/.cache/pypoetry/virtualenvs/pythonproject-9TtSrW0h-py3.11/lib/python3.11/site-packages/google/cloud/storage/fileio.py", line 357, in write
    self._upload_chunks_from_buffer(num_chunks)
  File "/root/.cache/pypoetry/virtualenvs/pythonproject-9TtSrW0h-py3.11/lib/python3.11/site-packages/google/cloud/storage/fileio.py", line 417, in _upload_chunks_from_buffer
    upload.transmit_next_chunk(transport, **kwargs)
  File "/root/.cache/pypoetry/virtualenvs/pythonproject-9TtSrW0h-py3.11/lib/python3.11/site-packages/google/resumable_media/requests/upload.py", line 503, in transmit_next_chunk
    method, url, payload, headers = self._prepare_request()
                                    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.cache/pypoetry/virtualenvs/pythonproject-9TtSrW0h-py3.11/lib/python3.11/site-packages/google/resumable_media/_upload.py", line 611, in _prepare_request
    raise ValueError("Upload has finished.")
ValueError: Upload has finished.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/app/main.py", line 31, in <module>
    with blob.open("wb", chunk_size=CHUNK_SIZE) as blob_writer:
  File "/root/.cache/pypoetry/virtualenvs/pythonproject-9TtSrW0h-py3.11/lib/python3.11/site-packages/google/cloud/storage/fileio.py", line 437, in close
    self._upload_chunks_from_buffer(1)
  File "/root/.cache/pypoetry/virtualenvs/pythonproject-9TtSrW0h-py3.11/lib/python3.11/site-packages/google/cloud/storage/fileio.py", line 417, in _upload_chunks_from_buffer
    upload.transmit_next_chunk(transport, **kwargs)
  File "/root/.cache/pypoetry/virtualenvs/pythonproject-9TtSrW0h-py3.11/lib/python3.11/site-packages/google/resumable_media/requests/upload.py", line 503, in transmit_next_chunk
    method, url, payload, headers = self._prepare_request()
                                    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.cache/pypoetry/virtualenvs/pythonproject-9TtSrW0h-py3.11/lib/python3.11/site-packages/google/resumable_media/_upload.py", line 611, in _prepare_request
    raise ValueError("Upload has finished.")
ValueError: Upload has finished.
```