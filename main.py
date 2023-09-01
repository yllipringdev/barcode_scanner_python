import cv2
import time
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

barcode_found = False

threshold = 3.0
start_time = time.time()

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)


    decoded_objects = decode(frame)

    for obj in decoded_objects:
        barcode_data = obj.data.decode('utf-8')
        print(barcode_data)

        barcode_found = True
        start_time = time.time()

    if barcode_found:
        break

    elapsed_time = time.time() - start_time
    if elapsed_time > threshold:
        cv2.putText(frame, "Please focus more, barcode not found", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
