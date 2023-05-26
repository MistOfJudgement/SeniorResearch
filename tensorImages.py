import pathlib
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
print("imported tf")
imagesPath = r"C:\Users\1499106\CompSciRes\nullpomino-master\nullpomino-run\target\install\ss"


def get_tensor_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_png(image)
    return image

def get_all_image_paths(image_folder):
    image_paths = []
    for path in pathlib.Path(image_folder).glob('*'):
        image_paths.append(str(path))
    return image_paths

def show_image(image):
    plt.imshow(image)
    plt.show()

image_paths = get_all_image_paths(imagesPath)
images = []
for image_path in image_paths:
    images.append(get_tensor_image(image_path))
