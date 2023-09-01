# barcode_scanner_python
This Python script utilizes OpenCV and the pyzbar library to create a simple barcode scanner. It captures video from your default camera (usually your webcam) and continuously searches for barcodes in the video feed. When a barcode is detected, it decodes the data and displays it on the console.


**Prerequisites**
Make sure you have the following libraries installed:

- OpenCV (cv2)
- pyzbar (pyzbar)

**Usage**
- Run the script.
- Point your camera towards a barcode.
- The script will display the camera feed and search for barcodes.
- When a barcode is found, its data will be printed in the console.
- You can exit the script by pressing the 'q' key.

If the script doesn't find a barcode within the specified time threshold (default is 3 seconds), it will display a message prompting you to focus more on the barcode.

Enjoy scanning barcodes with this simple Python script!
