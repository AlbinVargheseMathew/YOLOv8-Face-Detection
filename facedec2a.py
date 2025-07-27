from ultralytics import YOLO
import cv2

# Load model and initialize webcam
model = YOLO('face_yolov8n.pt')
cap = cv2.VideoCapture(0)

print("Press 'q' to quit, 's' to save a frame.")

save_count = 1  # Counter for saved frames

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Face detection
    results = model(frame)
    boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)

    # Draw face boxes
    for x1, y1, x2, y2 in boxes:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Face count box
    cv2.rectangle(frame, (10, 10), (180, 60), (50, 50, 50), -1)
    cv2.putText(frame, f"Faces: {len(boxes)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display output
    cv2.imshow("YOLOv8 Face Detection", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"frame_saved_{save_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved frame to {filename}")
        save_count += 1

    if key == ord('q') or cv2.getWindowProperty("YOLOv8 Face Detection", cv2.WND_PROP_VISIBLE) < 1:
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()