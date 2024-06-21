# Machine Learning FitFood

## Introduction

This project utilizes TensorFlow and pre-trained InceptionV3 for multi-label classification of food images. The dataset is divided into training, validation, and testing sets, resized, and normalized. The model is trained with additional custom layers, fine-tuned, and evaluated for accuracy. After training, it is converted to TensorFlow Lite (TFLite) for efficient food image predictions on Android mobile apps.

## Instructions for Using the Model

### Prerequisites
- Ensure you have Python installed.
- Install TensorFlow:
  ```bash
  pip install tensorflow
### Steps to Use the Model

1. **Download the Dataset:**
   - Download the data from the Google Drive link provided in the data folder.
   - Place the downloaded data into a new directory named `Dataset`.

2. **Clone the Repository:**
   - Clone our repository by running:
     ```bash
     git clone https://github.com/Alvinnxyz/Machine-Learning-FitFood.git
     ```
   - Place the `model.ipynb` file in the same directory as the `Dataset` folder.

3. **Run the Notebook:**
   - Execute the `model.ipynb` notebook to train and evaluate the model.

## Instructions for Using the FitFood Folder for API and Nutritional Database

The `fitfood` folder contains Python code with Django Rest Framework for deploying a search API and a food nutrition database.

### Steps to Use the API

1. **Clone the Repository:**
   - Follow the previous steps to clone the repository.

2. **Create a Virtual Environment:**
   - Install a virtual environment 
     ```bash
     pip install virtualenv
     ```
   - Create a virtual environment in the same directory by running:
     ```bash
     python -m venv (your_virtual_environment_name)
     ```
   - Activate the virtual environment and install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Server:**
   - Start the server by running:
     ```bash
     python manage.py runserver
     ```

5. **Deployment:**
   - For further steps, you can deploy the application on Google Cloud or any other deployment platform.

## Additional Information

For more details on how to use and deploy the model and API, please refer to the documentation in the respective folders.




untuk langkah lebih lanjut anda bisa melakukan deployment pada google cloud atau tempat deployment lainnya



