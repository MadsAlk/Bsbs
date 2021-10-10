from imutils import paths
import face_recognition
import pickle
import cv2 as cv
import os



def train():
    # Add your names, the same name of your folders
    current_names = os.listdir(f"{os.getcwd()}/CollectedData")
    predefined_encodings = []
    predefined_names = []

    for current_name in current_names:
        print(f"Start training process for {current_name}...")
        image_paths = list(paths.list_images(f"CollectedData/{current_name}"))
        print('image_paths........................', image_paths)
        # loop over the image paths
        for (i, image_path) in enumerate(image_paths):
            print(f"Processing image {i+1}")

            # load and convert image from BGR to RGB
            image = cv.imread(image_path)
            rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            boxes = face_recognition.face_locations(rgb, model="hog")
            encodings = face_recognition.face_encodings(rgb, boxes)

            for encoding in encodings:
                predefined_encodings.append(encoding)
                predefined_names.append(current_name)

    data = {"encodings": predefined_encodings, "names": predefined_names}
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()
