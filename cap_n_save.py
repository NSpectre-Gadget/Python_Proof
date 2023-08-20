def cap_n_save_pic():
    # creating a video object
    video = cv2.VideoCapture(0)
    # Setting Variable Count
    a = 0
    # While loop
    while True:
        a = a + 1
        # Create a frame object
        check, frame = video.read()
        # Converting to grayscale
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # show the frame!
        cv2.imshow("Capturing", frame)
        # for playing
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

        # Saving the image
        showPic = cv2.imwrite("filename.png", frame)
        print(showPic)

        # Shutting down the camera
        video.release()
        cv2.destroyAllWindows

        # read an image from a file using the cv2.imread() method
        imageB = cv2.imread("image.png")

        cv2.imshow("Image", imageB)
        cv2.waitKey(0)

        # load the images -- the original, the original + contrast,
        # and the original + photoshop
        original = cv2.imread("images/jp_gates_original.png")
        contrast = cv2.imread("images/jp_gates_contrast.png")
        shopped = cv2.imread("images/jp_gates_photoshopped.png")

    def mse(imageA, imageB):
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])

        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err


cap_n_save_pic()
mse()
