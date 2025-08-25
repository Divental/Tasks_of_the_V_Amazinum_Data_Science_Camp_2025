# Simple MNIST / Vision API Docker Project

This project contains a Python script (`lesson_24_task.py`) that performs a simple computer vision task (e.g., MNIST classification or image analysis) and can be run inside a Docker container.

## Docker Image

The project includes a `Dockerfile` based on `python:3.11-slim` that installs all required dependencies from `requirements.txt` and runs the script.

---

## Prerequisites

- Docker installed on your system
- Python installed if you want to run locally (optional)

---

## Build Docker Image

From the project directory (where `Dockerfile` is located), run:

```bash
docker build -t my-vision-app:latest .
```

##  Installation / Usage
1. Build the Docker Image

From the project directory, run:

```bash
docker build -t cv-task-image .
```

This will create a Docker image named cv-task-image.

2. Run the Container

To run the container:

```bash
docker run --rm cv-task-image
```

--rm automatically removes the container after it finishes execution.

The script lesson_24_task.py will execute inside the container.

3. Optional: Mount a folder for input/output

If your script requires input images or outputs results, you can mount a folder from your host machine:

```bash
docker run --rm -v /path/to/local/folder:/app/data cv-task-image
```

Replace /path/to/local/folder with your folder path.

Access this folder in your Python script as /app/data.

##   Example

If lesson_24_task.py reads an image from /app/data/input.png, runs processing, and saves result to /app/data/output.png, you can:

```bash
docker run --rm -v $(pwd)/data:/app/data cv-task-image
```

Then check the data folder on your host for the output.

##   Notes

* Make sure Python dependencies are listed in requirements.txt.

* You can modify lesson_24_task.py as needed and rebuild the image.

* The image is lightweight (~50-100 MB) thanks to python:3.11-slim.
