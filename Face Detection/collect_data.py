import cv2 as cv
import os



def shoot(name):
    path = os.getcwd()
    path2 = f"{path}/CollectedData/{name}"
    if os.path.isdir(path2) == False:
        os.mkdir(path2)
        
    #path = os.getcwd()
    #name = 'Ahmad'
    cam = cv.VideoCapture(0)
    img_counter = 0

    while True:
        is_success, frame = cam.read()
        if not is_success:
            print("failed to capture image.")
            break
        cv.imshow("Collecting Data by pressing space", frame)

        k = cv.waitKey(1)

        # Check if ESC is pressed
        if k%256 == 27:
            print("Press ESC to close...")
            break

        # Check if space is pressed
        elif k%256 == 32:
            img_name = f"{path}/CollectedData/{name}/{name}_img_{img_counter}.jpg"
            cv.imwrite(img_name, frame)
            print(f"Image #{img_counter} saved!")
            img_counter += 1

    cam.release()
    cv.destroyAllWindows()
