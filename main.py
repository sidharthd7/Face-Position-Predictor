import os
from PIL import Image
from landingai.predict import Predictor
from dotenv import load_dotenv

load_dotenv()

# Enter your API Key
endpoint_id = "075ce9bb-529c-4d14-8b9b-68b84936e759"
api_key = os.getenv("LANDING_AI_API_KEY")

# Run inference
predictor = Predictor(endpoint_id, api_key=api_key)

# Directory containing your images
base_directory = "dataset"

# Loop through each image in the directory
for subdir in os.listdir(base_directory):
    subdir_path = os.path.join(base_directory, subdir)
    
    if os.path.isdir(subdir_path):
        print(f"Processing images in directory: {subdir}")
        
    for image_name in os.listdir(subdir_path):
        if image_name.endswith(".jpg"):  
            image_path = os.path.join(subdir_path, image_name)
            try:
                image = Image.open(image_path)
            
                # Run inference
                predictions = predictor.predict(image)
            
                # Print or save the predictions for each image
                print(f"Predictions for {image_name} in {subdir}: {predictions}")
            
            except Exception as e:
                print(f"Error processing image {image_name}: {e}")
        