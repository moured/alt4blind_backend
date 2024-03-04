# Introduction
This repository contains the Python backend API code for the Alt4Blind project. The API receives an image (required) and an optional summary from the user, saves the received data in the "received" folder, and returns three similar images along with high-quality summaries.

# Files and Folders Explained
1. **dummy_data**: Contains ten chart images with summaries. The code randomly selects and returns three images from this folder.
2. **received**: Stores received data, including images and summaries.
3. **main.py**: Contains the code responsible for handling received requests.
4. **retrieval**: Contains the code responsible for analyzing received data and returning three images.

# How to Run
1. Prepare your Python environment. For example, activate your Conda workspace.
2. Install the required packages: ```pip install fastapi uvicorn```
3. Navigate to the project folder: ```cd <alt4blind_backend_path>```
4. Run the API: ```uvicorn main:app --reload --app-dir=.```
5.  You can now test the API from your frontend or another terminal. For example:
```
curl "http://localhost:8000/get-similar-images?image=iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAIAAAACUFjqAAAAEklEQVR4nGP8z4APMOGVHbHSAEEsAROxCnMTAAAAAElFTkSuQmCC&text=This is a test summary."
```

##### Note: In the above example, we send a small red image encoded in base64 along with the summary "This is a test summary."


