# 🌿 Potato Disease Prediction Web App

# 🏆 Overview

This project is a Potato Disease Prediction Web App built using Streamlit. The app allows users to upload an image of a potato leaf and predicts whether the leaf shows signs of:

🥀 Early Blight

🌧️ Late Blight

🍃 Healthy

# ✨ Features

🎨 User-Friendly Interface: Intuitive design for seamless image upload and prediction.

🔍 Accurate Disease Prediction: Classifies potato leaves into:

Potato__Early_blight

Potato_Late_blight

Potato__healthy

📊 Confidence Score: Displays prediction confidence level.

# 🛑 Diseases Explained

#  🥀 Early Blight

Cause: Caused by the fungus Alternaria solani.

Symptoms: Characterized by small, irregular brown spots with concentric rings on the leaves. Often begins with older leaves.

Impact: Can reduce photosynthesis, leading to decreased yield.

# 🌧️ Late Blight

Cause: Caused by the oomycete Phytophthora infestans.

Symptoms: Presents as large, irregular gray-green or brown water-soaked lesions. Can spread rapidly in wet conditions.

Impact: Extremely destructive, often resulting in complete crop loss if untreated.

# 🍃 Healthy

Description: Leaves are free from visible spots, lesions, or discoloration. Indicate optimal plant health.

# 💻 Technologies Used

Frontend: Streamlit for interactive UI.

Backend: TensorFlow and Keras for deep learning.

Language: Python.

Model: Custom CNN trained on potato leaf images.



# 📜Code Walkthrough

# 1. Input Layer

![Screenshot 2024-12-19 003414](https://github.com/user-attachments/assets/e06d54dc-99c0-451b-90dc-97b6686e962c)

Purpose: This layer is the entry point of the model.

What It Does: Accepts images of size 255x255 pixels with 3 channels (RGB for color images).

# 2. Preprocessing Layer

![Screenshot 2024-12-19 003437](https://github.com/user-attachments/assets/ebd93ed0-4281-42e8-af62-27e03341f1e2)


Purpose: Prepares the input image for further processing.

Steps:

Resizes images to the required dimensions.

Rescales pixel values to a range of 0 to 1 for numerical stability during training.

# 3. Convolutional Layers

# First Convolutional Block:

![Screenshot 2024-12-19 003500](https://github.com/user-attachments/assets/45701e9a-c189-418b-b8cb-bd0ba9c4396e)


Conv2D (32 filters):

Detects 32 features (like edges or simple textures) in the input image using a 3x3 filter.

ReLU Activation: Keeps only positive feature values, introducing non-linearity.

MaxPooling (2x2): Reduces the image size by summarizing each 2x2 block with the maximum value. This reduces computation and retains important information.

# Second Convolutional Block:

![Screenshot 2024-12-19 003508](https://github.com/user-attachments/assets/56bb4950-0706-4fd9-b457-b08ddd7ede9c)


Conv2D (64 filters):

Detects 64 more complex features, such as shapes or patterns.

MaxPooling: Again reduces the spatial dimensions, focusing on important details.

# Third Convolutional Block:

![Screenshot 2024-12-19 003514](https://github.com/user-attachments/assets/e8ced839-e5ba-4bf0-ba80-79297761184f)


Conv2D (128 filters):

Extracts higher-level features that distinguish specific objects in the image (e.g., disease-specific patterns).

MaxPooling: Further reduces the size to make computations efficient.

# 4. Flatten Layer

![Screenshot 2024-12-19 003522](https://github.com/user-attachments/assets/7b41052a-502e-489c-84dd-38796feb29c3)

Purpose: Converts the 3D feature maps (from convolutional layers) into a 1D vector.

# 5. Fully Connected (Dense) Layers

# First Dense Layer:

![Screenshot 2024-12-19 003528](https://github.com/user-attachments/assets/791bdb2d-03be-470d-a0ed-bfd8a7ad502c)

Purpose: Processes the flattened features and learns relationships between them.

What It Does: Contains 128 neurons to detect patterns across the extracted features.

# Output Layer:

![Screenshot 2024-12-19 003535](https://github.com/user-attachments/assets/c4ea174c-801a-4787-ac9e-e6236586e7a4)


Purpose: Provides the final classification result.
What It Does:

Outputs probabilities for 64 classes (e.g., 64 plant disease categories).

The Softmax Activation ensures the sum of probabilities is 1, helping to interpret the results.

# 🚀 How Web Application Works

📂 Image Upload: Upload a potato leaf image in jpg, jpeg, or png format.

🧠 AI Prediction: The app preprocesses the image and uses a deep learning model to predict the disease.

📈 Result Display: View the predicted class and confidence score.

# 🛠️ Installation

# 📋 Prerequisites

Python 3.7 or higher

Required libraries:

streamlit

tensorflow

numpy

📝 Steps

# 1.Clone the repository:

![Screenshot 2024-12-19 004048](https://github.com/user-attachments/assets/ff335233-bd68-40b2-bb9b-201fb77956ee)

# 2.Install dependencies:

![Screenshot 2024-12-19 004107](https://github.com/user-attachments/assets/76f6f096-2b3c-45d8-bbcb-0deaf5729f71)


# 3.Place the pre-trained model (model.h5) in the project directory.

# 4. Run the app:

![Screenshot 2024-12-19 004120](https://github.com/user-attachments/assets/284a877a-2f89-4ed0-a117-f4737ec9d4bf)

# 5.Access the app at http://localhost:8501.

# 📂 File Structure

potato(app).py: Main Streamlit app script.

model.h5: Pre-trained TensorFlow model.

requirements.txt: Python dependencies.

# 📊 Dataset

The model was trained on a curated dataset of potato leaf images, covering:

Early Blight

Late Blight

Healthy leaves

# 🎯 Usage

Launch the app.

Upload a clear potato leaf image.

Click Predict.

View the prediction and confidence score.

# 📸 Example Output

![Screenshot 2024-12-19 005304](https://github.com/user-attachments/assets/4104e88d-d330-4b2c-baac-a2d0745c6041)
















