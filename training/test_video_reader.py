import cv2

# Sample input used to verify that OpenCV can decode the uploaded video.
video_path = "uploads/test_video.mp4"

# VideoCapture provides sequential access to decoded frames.
cap = cv2.VideoCapture(video_path)

# Count successfully decoded frames for comparison with expected video length.
frame_count = 0

while True:

    # success becomes False when the stream ends or a frame cannot be decoded.
    success, frame = cap.read()

    if not success:
        break

    frame_count += 1

    # Printing the shape verifies height, width, and color channels are present.
    print(
        f"Frame {frame_count}: {frame.shape}"
    )

# Release the underlying file/decoder handle after iteration.
cap.release()

print(
    f"Total Frames: {frame_count}"
)
