import os
import io
import base64
import random
from PIL import Image
import json

def get_similar_images(base_image: Image.Image, text) -> dict:
    # List all files in the images folder
    data_folder = '/home/omoured/Downloads/alt4blind_api/dummy_data'
    image_files = [file for file in os.listdir(data_folder) if file.endswith('.png')]
    
    # Randomly select three unique file names
    random_images = random.sample(image_files, 3)
    
    images = []
    for image_file in random_images:
            # Convert image data to PIL Image and convert to RGB mode
            pil_image = Image.open(os.path.join(data_folder, image_file)).convert("RGB")
            
            # Convert PIL Image to base64 encoded string
            buffered = io.BytesIO()
            pil_image.save(buffered, format="PNG")
            encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
            
            # Load summary from txt file
            text_file = image_file.replace(".png",".txt")
            with open(os.path.join(data_folder,text_file), 'r') as summary_file:
                summary = summary_file.read()
            
            images.append({"image": encoded_image, "summary": summary})
    
    return json.dumps({"images": images})
