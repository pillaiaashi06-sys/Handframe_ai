
import cv2
import mediapipe as mp
import numpy as np

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Could not open webcam.")

# Initialize hand tracking
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Starting position and size of the frame
center_x, center_y = 320, 240
frame_width = 300

try:
    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6
    ) as hands:

        while True:
            success, frame = camera.read()

            if not success:
                break

            # Mirror webcam view
            frame = cv2.flip(frame, 1)
            height, width = frame.shape[:2]

            # Keep an unmodified copy of the live image
            original = frame.copy()

            # Prepare image for MediaPipe
            rgb = cv2.cvtColor(
                original, cv2.COLOR_BGR2RGB
            )
            results = hands.process(rgb)

            if results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]

                # Index fingertip
                index = hand.landmark[8]
                ix = int(index.x * width)
                iy = int(index.y * height)

                # Thumb tip
                thumb = hand.landmark[4]
                tx = int(thumb.x * width)
                ty = int(thumb.y * height)

                # Move frame using index finger
                center_x = ix
                center_y = iy

                # Finger distance controls frame size
                distance = np.hypot(ix - tx, iy - ty)

                max_width = max(
                    1,
                    min(420, width - 10,
                        int((height - 10) / 0.62))
                )

                min_width = min(180, max_width)

                frame_width = int(np.clip(
                    180 + distance * 1.5,
                    min_width,
                    max_width
                ))

                frame_height = max(
                    1, int(frame_width * 0.62)
                )

                # Calculate frame boundaries
                x1 = int(np.clip(
                    center_x - frame_width // 2,
                    0, width - frame_width
                ))
                y1 = int(np.clip(
                    center_y - frame_height // 2,
                    0, height - frame_height
                ))

                x2 = x1 + frame_width
                y2 = y1 + frame_height

                # Crop the LIVE webcam area inside the frame
                crop = original[y1:y2, x1:x2]

                if crop.size > 0:
                    # Convert crop to grayscale
                    gray = cv2.cvtColor(
                        crop, cv2.COLOR_BGR2GRAY
                    )

                    # Create a thermal heatmap
                    heatmap = cv2.applyColorMap(
                        gray, cv2.COLORMAP_JET
                    )

                    # Draw a holographic grid
                    grid = heatmap.copy()
                    step = 25

                    for x in range(0, frame_width, step):
                        cv2.line(
                            grid,
                            (x, 0),
                            (x, frame_height - 1),
                            (255, 70, 255), 1
                        )

                    for y in range(0, frame_height, step):
                        cv2.line(
                            grid,
                            (0, y),
                            (frame_width - 1, y),
                            (255, 70, 255), 1
                        )

                    # Blend grid with the heatmap
                    heatmap = cv2.addWeighted(
                        grid, 0.35, heatmap, 0.65, 0
                    )

                    # Put heatmap inside the virtual frame
                    frame[y1:y2, x1:x2] = heatmap

                # Add neon pink frame border
                cv2.rectangle(
                    frame,
                    (x1 - 2, y1 - 2),
                    (x2 + 2, y2 + 2),
                    (255, 0, 255), 3
                )

                # Draw hand landmarks
                mp_draw.draw_landmarks(
                    frame,
                    hand,
                    mp_hands.HAND_CONNECTIONS
                )

                message = "Move index finger | Spread fingers to resize"

            else:
                message = "Show your hand to control the frame"

            # Add interface label
            cv2.putText(
                frame,
                "HANDFRAME AI | THERMAL / HEATMAP",
                (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                message,
                (15, height - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (255, 255, 255),
                1
            )

            cv2.imshow("HandFrame AI - Thermal Frame", frame)

            # Press Q to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

finally:
    camera.release()
    cv2.destroyAllWindows()
