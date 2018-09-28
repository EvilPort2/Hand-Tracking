import cv2
import numpy as np
import glob

def save_image(img, index):
	cv2.imwrite('augmented/augmented_image%d.jpg'%(index,), img)

def augment_color(img):
	h, w, c = img.shape
	randomColor = np.array((np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), dtype=np.uint8)
	randomColorImage = np.zeros(shape=(h, w, c), dtype=np.uint8) + randomColor
	img = cv2.addWeighted(img,0.8,randomColorImage,0.2,0)
	return img

def augment_size(img):
	x = np.random.randint(50, 150)
	y = np.random.randint(50, 150)
	img = cv2.resize(img, (x, y))
	return img

def augment_noise(img):
	h, w, c = img.shape
	noise = np.random.randn(h, w, c)
	flat_noise = noise.flatten()
	noise_min = min(flat_noise)
	noise_max = max(flat_noise)
	noise = (noise - noise_min)/(noise_max - noise_min)
	noise = (noise*255).astype(np.uint8)
	img = cv2.addWeighted(img, 0.7, noise, 0.3, 0)
	return img

def augment_rotation(img):
	h, w, c = img.shape
	randomDegree = np.random.randint(1, 10)
	M = cv2.getRotationMatrix2D((h/2 , w/2), randomDegree , 1)
	img = cv2.warpAffine(img, M, (h, w))
	return img

def augment_flip(img):
	flipCodes = [0, 1, -1]
	randomFlipCode = flipCodes[np.random.randint(0, 3)]
	img = cv2.flip(img, randomFlipCode)
	return img

def no_augment(img):
	return img

def main():
	augmentations = [augment_color, augment_flip, augment_rotation, augment_size, augment_noise, no_augment]
	offset = 0
	for n, image in enumerate(glob.glob('unlabelled_images/*.jpg')):
		noOfAugmentations = np.random.randint(0, len(augmentations))
		img = cv2.imread(image)
		for i in range(noOfAugmentations):
			randomAugmentation = augmentations[np.random.randint(0, len(augmentations))]
			img = randomAugmentation(img)
		save_image(img, n+offset)

if __name__ == '__main__':
	main()
	'''img = cv2.imread('unlabelled_images/image4.jpg')
	cv2.imshow('noisy', augment_noise(img))
	cv2.waitKey(0)'''
