# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2


class Person:
    def _init_(
        self, first_name, last_name, image, height_ft, height_in, race, license_number
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.image = image
        self.height_ft = height_ft
        self.height_in = height_in
        self.race = race
        self.license_number = license_number


class address:
    address_line_1: str
    address_line_2: str
    city: str
    state: str
    country: str
    postal_code: str

    def get_full_address(self) -> str:
        return f"{self.address_line_1}, {self.address_line_2}, {self.city},{self.state}, {self.country}, {self.postal_code}"

    # def match (self, image):

    def take_picture():
        camera = cv2.VideoCapture(0)
        i = 0
        while i < 2:
            raw_input("Press Enter to capture")
            return_value, image = camera.read()
            cv2.imwrite("opencv" + str(i) + ".png", image)
            i += 1
        del camera

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


owner1 = Person("Zachary", "Butler", image.png, 5, 10, "black", E60101823)
secondary_user1 = Person("", "", image, 5, 7, Asian, E13248488)


registered_owner = Person()
image = Person()
access_date = Person()


print(Person.self)
