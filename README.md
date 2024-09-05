# PDF Interpreter - Preprocessing documents by reading charts and translating to English
## Running instructions
Navigate to the repository and then execute the following instructions:
```bash
docker build -t pdf-translator .
docker run -v <local path to files to translate>:/data -v <local path to save translated files>:/processed_data pdf-translator /data

