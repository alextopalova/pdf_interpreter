# PDF Interpreter - Preprocessing documents by reading charts and translating to English
## Running instructions
Navigate to the repository and then execute the following instructions:
```bash
docker build -t pdf-translator .
docker run -v <Path_to_files>:/data pdf-translator /data

