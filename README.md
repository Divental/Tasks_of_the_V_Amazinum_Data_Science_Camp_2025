# Simple MNIST Computer Vision API

## Overview
This project provides a simple computer vision solution for recognizing handwritten digits using the MNIST dataset.  
It is deployed as a **FastAPI** service that accepts an image and predicts the digit.

---

## Deployment Info
The API can be run locally using **Uvicorn**:

```bash
uvicorn app:app --reload
Once running, the endpoints are available at:
```
* GET / — health check

* POST /predict/ — predict digit from an uploaded image

## Installation
1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_folder>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the API:

```bash
uvicorn app:app --reload
```

## Modeling Info
Dataset: MNIST (handwritten digits 0–9)

* Model Architecture:

* Flatten layer (28x28 → 784)

    * Dense 128 units, ReLU activation

    * Dense 10 units, softmax activation

    * Training: 1 epoch (for demonstration)

* Saved Model File: mnist_model.h5

* If ```mnist_model.h5``` does not exist, the API automatically trains the model on the first run.

##   Example Process

1. Start the API:

```bash
uvicorn app:app --reload
```

2. Open Swagger UI at http://127.0.0.1:8000/docs
 to test endpoints interactively.

3. Example curl request for prediction:

```bash
curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@sample_image.png"
```

Example Response:

``` {"predicted_digit": 7}``` 

##  Notes
* Make sure python-multipart is installed to handle file uploads.

* The model trains automatically if the saved model file mnist_model.h5 is missing.

* This setup is for demonstration purposes; for production, use a fully trained model and proper error handling.