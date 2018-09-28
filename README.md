# Hand Tracking
Tracking hands using SSD with MobilenetV1

## Outcome
See it <a href='https://youtu.be/RZqK-q1QFFI'>here</a>

## What I did here
1. Recorded images of my hands in different postures, positions and background.
2. Randomly did some augmentations to those images viz resize, coloration, add noise, flip and rotate.
3. Used Tensorflow's object detection API for training SSD with MobilnetV1.

## Generation and annotation of dataset
1. I generated the dataset myself. The model trained by victordibia did not work for me. So I had to generate data by myself and annotate them.
2. Got some images from the camera of hand in different postures, positions and background using the get_camera_images.py. The pictures are stored in unlabelled_images/ folder.
3. Now I do some image augmentations on the previous images. The augmentations are selected randomly selected by the program augment_images.py. The augmented images are stored in augmented/ folder.
4. Now I annotate the augmented images using the labelImg program by tzutalin.

## How to train
Follow this tutorial by sentdex <a href='https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/'>here</a>

## What is the intention behind this project
The main intention behind the project is my sign language project. Many of you complained that the skin detection using histogram backprojection does not work well for you. So I decided to go for hand detection instead of skin colour detection. So you can expect a lot of changes in the sign language program within the mext couple of months.

## Credits
1. sentdex for the Tensorflow Object Detection API Tutorial <a href='https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/'>here</a>
2. datitran for the generate_tfrecords.py and xml_to_csv.py
3. victordibia for the original inspiration.
4. tzutalin for labelImg