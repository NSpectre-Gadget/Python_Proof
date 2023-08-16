# import the necessary packages
from driver_dictionary import driver_dictionary
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pygame
import pygame.camera
import requests
import creds
import sys

# accept the image e.g. "house1.png" from the user


# secondary_user1 = Person("", "", image, 5, 7, Asian, E13248488)


# registered_owner = Person("Zachary", "Butler", image.png, 5, 10, "black", E60101823)
# driver = user()
# imageA = Person("Zachary", "Butler", image.png, 5, 10, "black", E60101823)
# access_date = Person("Zachary", "Butler", image.png, 5, 10, "black", E60101823)


class Person:
    driver_dictionary()
    #    x = int(input("Enter no. of drivers allowed: ").strip())
    #    d = {}

    #    for i in range(x):
    #        first_name = input("Enter your first name: ")
    #        last_name = input("Enter your last name")
    #        imageB = raw_input("enter the name of the image file: ")
    # imageA = Image.open(sys.argv[1])
    #        height = input("Enter your height in ft and inches: ")
    #        race = input("Enter your race: ")
    #        dl_number = input("Enter your driver's license number: ")
    #        driver = input().split("")
    #        driver_info = int(input())
    #        d[driver[0]] = driver[1], driver[2], driver[3], driver[4], driver[5], driver[6]
    #    print(d)

    def _init_(
        self, first_name, last_name, imageB, height_ft, height_in, race, license_number
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.imageb = imageb
        self.height_ft = height_ft
        self.height_in = height_in
        self.race = race
        self.license_number = license_number

    def ID_source(self):
        name = self.Person()
        print(name)

    def ID_print(self):
        print(first_name, last_name, imageB, height_ft, height_in, race, license_number)


def create_session():
    s = requests.Session()
    s.headers.update(
        {"X-Shopify-Accccess-Token": creds.token, "Content-Type": "application/json"}
    )
    return s


def main():
    sess = create_session()
    resp = sess.get(creds.url + "/admin/api/2021-07/products.json?limit=10")
    print(sresp.json())
    owner1 = Person()
    owner1.ID_print()


if _name_ == "_main_":
    Person()


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

    def compare_images(imageA, imageB, title):
        # compute the mean squared error and structural similarity
        # index for the images
        m = mse(imageA, imageB)
        s = ssim(imageA, imageB)
        # setup the figure
        fig = plt.figure(title)
        plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
        # show first image
        ax = fig.add_subplot(1, 2, 1)
        plt.imshow(imageA, cmap=plt.cm.gray)
        plt.axis("off")
        # show the second image
        ax = fig.add_subplot(1, 2, 2)
        plt.imshow(imageB, cmap=plt.cm.gray)
        plt.axis("off")
        # show the images
        plt.show()

    # load the images -- the original, the original + contrast,
    # and the original + photoshop
    original = cv2.imread("images/jp_gates_original.png")
    contrast = cv2.imread("images/jp_gates_contrast.png")
    shopped = cv2.imread("images/jp_gates_photoshopped.png")
    # convert the images to grayscale
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
    shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

    def image_compare():
        # initializing  the camera
        pygame.camera.init()

        # make the list of all available cameras
        camlist = pygame.camera.list_cameras()

        # if camera is detected or not
        if camlist:
            # initializing the cam variable with default camera
            cam = pygame.camera.Camera(camlist[0], (640, 480))

            # opening the camera
            cam.start()

            # capturing the single image
            image = cam.get_image()

            # saving the image
            pygame.image.save(image, "filename.jpg")

        # if camera is not detected the moving to else part
        else:
            print("No camera on current device")


def main():
    driver = Person()
    print(driver.imageB)
    print(driver.imageA)


print("ID analysis complete")
