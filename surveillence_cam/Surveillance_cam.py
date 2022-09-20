import cv2
import socket

# Amount frame needs to change between current and latest to be considered motion True 
threshold = 450000

record_buffer_max = 15 
record_buffer = 0

def capture_video_ex():
    vid = cv2.VideoCapture(0)

    while True:
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
  
        # Display the resulting frame
        cv2.imshow('frame', frame)
      
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    print("Runs")

    capture_video_ex()

    #if not os.path.isdir("output_files"):
    #    os.makedirs("output_files")
