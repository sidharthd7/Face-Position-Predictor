import os
from PIL import Image
from landingai.predict import Predictor
from dotenv import load_dotenv

load_dotenv()

# Enter your API Key
endpoint_id = "075ce9bb-529c-4d14-8b9b-68b84936e759"
api_key = "LANDING_AI_API_KEY"

# Load your image
image = Image.open("image.png")

# Run inference
predictor = Predictor(endpoint_id, api_key=api_key)

image_directory = "path_to_your_images"

# Loop through each image in the directory
for image_name in os.listdir(image_directory):
    if image_name.endswith(".png"):  # or ".jpg", ".jpeg"
        image_path = os.path.join(image_directory, image_name)
        image = Image.open(image_path)
        
        # Run inference
        predictions = predictor.predict(image)
        
        # Print or save the predictions for each image
        print(f"Predictions for {image_name}: {predictions}")
        