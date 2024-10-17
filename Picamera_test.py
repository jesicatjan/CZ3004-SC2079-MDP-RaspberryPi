import os
import requests
from picamera import PiCamera
from time import sleep

# Define the camera and output file
camera = PiCamera()
image_path = '18102024_4_C.jpg'

try:
    # Step 1: Capture the image using the legacy camera stack (picamera library)
    print("Capturing image...")
    sleep(2)  # Give the camera some time to adjust
    camera.capture(image_path)
    print("Image captured successfully.")
    
    # Step 2: Send the captured image to the API
    ALGO_API_IP = "192.168.31.24"
    ALGO_API_PORT = "5000"
    url = f"http://{ALGO_API_IP}:{ALGO_API_PORT}/image"
    
    # Ensure the file is specified correctly and opened with 'rb' mode
    with open(image_path, 'rb') as img_file:
        print("Sending image to the API...")
        # The files parameter should include the filename and the file object
        response = requests.post(url, files={"file": (image_path, img_file)})
        
        # Step 3: Check and print the API response
        if response.status_code == 200:
            print("Image successfully sent to the API.")
            print("API Response:", response.json())
        else:
            print("Failed to send image to the API.")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
            
except FileNotFoundError:
    print("Failed to capture image. File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    camera.close()

