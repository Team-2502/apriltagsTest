# import the necessary packages
import apriltag
import cv2




vid = cv2.VideoCapture(0)

vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1)

while(True):

	ret, frame = vid.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	options = apriltag.DetectorOptions(families="tag36h11", quad_decimate=5.0,
            nthreads=4)
	detector = apriltag.Detector(options)
	results = detector.detect(gray)
	# loop over the AprilTag detection results
    for (r) in results {
            print(r)

            }

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
