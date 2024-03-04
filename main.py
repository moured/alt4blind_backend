from fastapi import FastAPI, HTTPException, Query
from io import BytesIO
import base64
from PIL import Image
from retrieval import get_similar_images

app = FastAPI()

def decode_image(image_base64: str) -> Image.Image:
    image_data = BytesIO(base64.b64decode(image_base64))
    return Image.open(image_data).convert("RGB")

@app.get("/get-similar-images")
def process_image(image= Query(None, alias="image"), summary=Query(None, alias="summary")):
    try:
        if not image:
            raise HTTPException(status_code=400, detail="The Image is missing!")
        
        decoded_image = decode_image(image)
        print('image received and decoded.')
        
        Image.open(BytesIO(base64.b64decode(image))).convert("RGB").save("received/received_image.png")
        print('received image is saved to received file')
        
        with open("received/received_summary.txt", "a") as summary_file:
            summary_file.write(summary + "\n")
        print('Received summary is appended to received_summary.txt.')

        images_data = get_similar_images(decoded_image, summary)
        return images_data
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
