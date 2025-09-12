import os

# === Get absolute path to current config file directory ===
current_dir = os.path.dirname(os.path.abspath(__file__))

# === Dataset Path Settings ===
# All paths are relative to this config file location
### TODO: Update these paths according to your file structure
PDF_PATH = os.path.join(current_dir, "data/input/pdfs")  # Raw input PDFs
PDF_IMAGE_PATH = os.path.join(current_dir, "data/processed/parent_images")  # Converted PDF page images
TEM_IMAGE_PATH = os.path.join(current_dir, "data/processed/child_images")  # Cropped TEM sub-images
DESCRIPTION_PATH = os.path.join(current_dir, "data/processed/descriptions")  # Cropped captions

# === YOLO Model Weights ===
### TODO: Place your trained model files in the models directory
CROP_IMAGES = os.path.join(current_dir, "models/yolo/crop_images.pt")             # For detecting main panels
IMAGE_DESCRIPTION = os.path.join(current_dir, "models/yolo/image_description.pt") # For splitting TEM vs caption
TEM_IMAGE_CROP = os.path.join(current_dir, "models/yolo/tem_image_crop.pt")       # For cropping sub-TEM structures

# === Classification Models (ResNet-based) ===
### TODO: Place your trained classifier files in the models directory
BINARY_CLASSIFIER = os.path.join(current_dir, "models/classifiers/binary_classifier.pth")    # None vs NotNone classifier
FIVE_CLASS_CLASSIFIER = os.path.join(current_dir, "models/classifiers/five_class_classifier.pth")  # 5-way TEM classifier


# === CSV Output Path ===
CSV_PATH = os.path.join(current_dir, "output/tem_images_description.csv")  # Metadata logging

if __name__ == '__main__':
    print(current_dir)