import cv2


# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cv2.aruco markers
    cv2.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    parameters = cv2.aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, cv2.aruco_dict, parameters=parameters)
    
    if ids is not None:
            print(corners)
            print(type(corners))
            cv2.aruco.drawDetectedMarkers(frame, corners)
            

    # Display the frame
    cv2.imshow('frame', frame)

    # Check for key press
    key = cv2.waitKey(1)
    if key == 27:  # Press 'esc' to exit
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
