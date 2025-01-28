# PlantMedix

PlantMedix is a machine learning application designed to assist farmers and agricultural experts in identifying plant diseases from leaf images using Convolutional Neural Networks (CNN). By analyzing uploaded images of plant leaves, the app can predict whether the plant is healthy or affected by a disease, enabling quick and accurate assessments of plant health.

## Dataset Source
The dataset used for this project is the PlantVillage Dataset, which contains images of both healthy and diseased plants from 38 different classes. These images represent various plant species and their corresponding diseases, forming a comprehensive collection to train the model. You can find the dataset [here](https://github.com/spMohanty/PlantVillage-Dataset).

## Project Workflow

1. **Data Extraction**: The PlantVillage dataset is processed by extracting and organizing images according to plant species and disease categories.
   
2. **Data Preprocessing**: Each image is resized to 224x224 pixels to match the expected input size of the CNN model. Data augmentation techniques, such as random rotations and flips, are applied to ensure the model generalizes well.
   
3. **Data Preparation**: The dataset is split into 80% training and 20% validation sets. Image data generators are employed to handle the images efficiently during training and testing.
   
4. **Model Development**: A CNN model is constructed with multiple convolutional layers followed by dense layers for classification. The CNN architecture is designed to extract key features from plant leaf images to classify them accurately into different categories (healthy or diseased).
   
5. **Model Training**: The model is trained for 5 epochs, achieving a validation accuracy of **88.11%**. This training allows the model to recognize various diseases in plant leaves and distinguish them from healthy plants.
   
6. **Model Evaluation**: After training, the model's performance is evaluated using accuracy and loss metrics. The model achieves a solid performance on validation data, showing its potential for real-world applications.
   
7. **Building a Classifier System**: A Classifying function is built to process uploaded plant leaf images, classify them as either healthy or diseased, and provide the result. This system is integrated into a user-friendly Streamlit app for real-time predictions.
   
8. **Deployment **: The trained model is deployed using Streamlit, allowing users to upload images, view predictions, and get quick diagnoses of plant health.

## Performance Metrics
- **Validation Accuracy**: **88.11%**
- **Validation Loss**: **0.5387**



