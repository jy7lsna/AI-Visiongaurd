import cv2
import face_recognition
import serial
import time

# Serial connection with Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)  
time.sleep(2)

# Load and encode the authorized face
authorized_image = face_recognition.load_image_file("user1.jpg")
authorized_encodings = face_recognition.face_encodings(authorized_image)

if not authorized_encodings:
    print("Error: No face detected in user1.jpg!")
    exit()

authorized_face_encoding = authorized_encodings[0]

# Open the webcam
cap = cv2.VideoCapture(0)

last_state = None
frame_skip = 2  # Skip every 2nd frame to speed up processing
frame_count = 0  

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue  # Skip this frame

    # Reduce frame size for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Detect faces
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    if face_encodings:  # If at least one face is detected
        authorized_detected = False

        for face_encoding in face_encodings:
            distance = face_recognition.face_distance([authorized_face_encoding], face_encoding)[0]
            if distance < 0.5:
                authorized_detected = True
                break

        # Avoid sending duplicate signals
        if authorized_detected and last_state != "authorized":
            arduino.write(b'1')
            print("✅ Authorized")
            last_state = "authorized"
        elif not authorized_detected and last_state != "unauthorized":
            arduino.write(b'0')
            print("❌ Unauthorized")
            last_state = "unauthorized"
    
    else:  # No face detected
        if last_state != "no_face":
            arduino.write(b'0')  # Keep the system locked
            print("🚫 No Face Detected")
            last_state = "no_face"

    # Show bounding box
    for (top, right, bottom, left) in face_locations:
        color = (0, 255, 0) if authorized_detected else (0, 0, 255)
        cv2.rectangle(frame, (left * 2, top * 2), (right * 2, bottom * 2), color, 2)  # Scale back to full size

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()

