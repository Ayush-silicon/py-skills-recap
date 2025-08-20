import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

# Initialize webcam
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    raise Exception("Error: Could not open webcam. Check camera connection.")

def load_face_encoding(image_path, name):
    """Helper function to load an image and return its face encoding safely."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) == 0:
        raise ValueError(f"No face found in {image_path} for {name}")

    return encodings[0]

# Load known faces
ayan_face_encoding = load_face_encoding("images/ayush.jpg", "Ayan")
rohit_face_encoding = load_face_encoding("images/rohit.jpg", "Rohit")

known_face_encodings = [ayan_face_encoding, rohit_face_encoding]
known_face_names = ["Ayan", "Rohit"]

# Students list (copy to track remaining)
students = known_face_names.copy()

# Date for attendance file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
writer = csv.writer(f)
writer.writerow(["Name", "Time"])  # CSV header

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to grab frame")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            # Mark attendance only once
            if name in students:
                students.remove(name)
                current_time = now.strftime("%H:%M:%S")
                writer.writerow([name, current_time])
                print(f"{name} marked present at {current_time}")

            # Draw label on the video
            top, right, bottom, left = [v * 4 for v in face_locations[0]]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.9, (255, 255, 255), 2)

    cv2.imshow("Attendance", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
