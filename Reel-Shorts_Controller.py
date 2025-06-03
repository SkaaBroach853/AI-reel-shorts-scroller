import cv2
import mediapipe as mp
import pyautogui
import time

class FaceControlShorts:
    def __init__(self):
        # Initialize webcam
        self.cam = cv2.VideoCapture(0)
        if not self.cam.isOpened():
            print("Error: Could not open webcam.")
            exit()

        # Initialize face mesh detector
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        # Initialize hand detector
        self.hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.mp_drawing = mp.solutions.drawing_utils
        # Cooldown to prevent multiple triggers
        self.last_action = 0
        self.cooldown = 0.005  # Cooldown time in seconds
        
        # Movement thresholds for gestures
        self.movement_threshold = 0.035  # Threshold for detecting finger movement
        self.mouth_open_threshold = 0.04 # Threshold for detecting mouth open

        # Store previous y positions for index finger and thumb
        self.prev_y_index = None
        self.prev_y_thumb = None

        # For pinch-to-zoom (kept as placeholder, but not actively used for control)
        self.initial_pinch_distance = None
        self.zoom_sensitivity = 0.05 # Adjust as needed

    # --- Helper function for distance calculation ---
    def euclidean_distance(self, p1, p2):
        return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

    # --- Mouth Detection ---
    def detect_mouth_open(self, landmarks):
        # Upper and lower lip points (landmarks 13 and 14)
        upper_lip = landmarks[13]
        lower_lip = landmarks[14]
        return (lower_lip.y - upper_lip.y) > self.mouth_open_threshold

    # --- Index Finger Movement Detection ---
    def detect_index_finger_down_movement(self, hand_landmarks):
        if not hand_landmarks:
            self.prev_y_index = None
            return False

        # Get index finger tip position (landmark 8)
        index_finger = hand_landmarks.landmark[8]
        
        downward_movement = False
        
        if self.prev_y_index is not None:
            # Check if index finger moved downward
            if index_finger.y - self.prev_y_index > self.movement_threshold:
                downward_movement = True
        
        self.prev_y_index = index_finger.y
        return downward_movement

    # --- Thumb Movement Detection ---
    def detect_thumb_down_movement(self, hand_landmarks):
        if not hand_landmarks:
            self.prev_y_thumb = None
            return False

        # Get thumb tip position (landmark 4)
        thumb_tip = hand_landmarks.landmark[4]
        
        thumb_downward_movement = False
        
        if self.prev_y_thumb is not None:
            # Check if thumb moved downward
            if thumb_tip.y - self.prev_y_thumb > self.movement_threshold:
                thumb_downward_movement = True
        
        self.prev_y_thumb = thumb_tip.y
        return thumb_downward_movement

    # --- Pinch-to-Zoom Detection (Conceptual - not used for control in this version) ---
    def detect_pinch_zoom(self, hand_landmarks):
        if not hand_landmarks:
            self.initial_pinch_distance = None
            return None # No pinch detected

        thumb_tip = hand_landmarks.landmark[4]
        index_tip = hand_landmarks.landmark[8]

        current_distance = self.euclidean_distance(thumb_tip, index_tip)

        if self.initial_pinch_distance is None:
            # If fingers are relatively close, consider it the start of a pinch gesture
            if current_distance < 0.1: # Arbitrary small distance to start tracking
                self.initial_pinch_distance = current_distance
                return "start"
        else:
            # Check for zoom in (distance increases) or zoom out (distance decreases)
            if current_distance - self.initial_pinch_distance > self.zoom_sensitivity:
                self.initial_pinch_distance = current_distance # Update initial distance to prevent continuous trigger
                return "zoom_in"
            elif self.initial_pinch_distance - current_distance > self.zoom_sensitivity:
                self.initial_pinch_distance = current_distance # Update initial distance
                return "zoom_out"
            # If the distance change is not significant enough, maintain the initial distance
            # This prevents resetting the gesture if there's minor finger movement
            elif abs(current_distance - self.initial_pinch_distance) < self.zoom_sensitivity / 2:
                return "maintaining"
            else:
                # If the distance changes significantly but not enough for a zoom, reset
                self.initial_pinch_distance = None
                return None
        return None

    def start(self):
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("Error: Failed to grab frame.")
                break

            # Flip the frame horizontally for a natural selfie-view display
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame with MediaPipe Face Mesh
            results_face_mesh = self.face_mesh.process(rgb_frame)
            # Process the frame with MediaPipe Hands
            results_hands = self.hands.process(rgb_frame)

            # Convert back to BGR for OpenCV display
            image = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

            # --- Face Mesh (Mouth Control) ---
            if results_face_mesh.multi_face_landmarks:
                for face_landmarks in results_face_mesh.multi_face_landmarks:
                    # Draw face landmarks (optional)
                    self.mp_drawing.draw_landmarks(image, face_landmarks, mp.solutions.face_mesh.FACEMESH_CONTOURS)

                    # Mouth control for next Short
                    if self.detect_mouth_open(face_landmarks.landmark) and (time.time() - self.last_action) > self.cooldown:
                        pyautogui.press('down')
                        print("Mouth Open: Next Short")
                        self.last_action = time.time()

            # --- Hand Landmarks (Index Finger and Thumb Control) ---
            if results_hands.multi_hand_landmarks:
                for hand_landmarks in results_hands.multi_hand_landmarks:
                    # Draw hand landmarks (optional)
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

                    # Index finger control for previous Short
                    if self.detect_index_finger_down_movement(hand_landmarks) and (time.time() - self.last_action) > self.cooldown:
                        pyautogui.press('up')
                        print("Index Finger Down: Previous Short")
                        self.last_action = time.time()

                    # Thumb control for next Short
                    if self.detect_thumb_down_movement(hand_landmarks) and (time.time() - self.last_action) > self.cooldown:
                        pyautogui.press('down')
                        print("Thumb Down: Next Short")
                        self.last_action = time.time()

            # Display the frame
            cv2.imshow('Eye and Hand Control for YouTube Shorts', image)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        self.cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_control = FaceControlShorts()
    face_control.start()