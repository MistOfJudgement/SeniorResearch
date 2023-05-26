#screenshot of google window
from cProfile import label
import win32gui
from PIL import ImageGrab
import time
import tensorflow as tf


def getHandle(windowName):
    return win32gui.FindWindow(None, windowName)

model = tf.keras.models.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(480, 640, 3)),
    tf.keras.layers.Conv2D(16, 3, padding="same", activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, 3, padding="same", activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, padding="same", activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(30)
])
model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
model.load_weights("./checkpoint/cp.ckpt")

labels = [0,1,2,3,4,5,6,8,9,10,12,16,17,18,19,20,22,24,32,33,34,36,40,128,132,136,160,164,168,256]
print(len(labels))
buttonMap = {
    0: "",
    1: "Hard",
    2: "Soft",
    4: "Left",
    8: "Right",
    16: "RotL",
    32: "RotR",
    64: "huh",
    128: "hold",
    256: "Rot180",
    512: "huuuuh",
}

def screenshot(hwnd):
    # get the size of the window
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    top = top+ 31
    left = left + 8
    width = 640
    height = 480
    right = left + width
    bottom = top + height
    # bring to foreground
    win32gui.SetForegroundWindow(hwnd)
    #20ms delay
    time.sleep(0.02)
    # take a screenshot
    im = ImageGrab.grab(bbox=(left, top, right, bottom))
    image_array = tf.keras.preprocessing.image.img_to_array(im)
    prediction = model.predict(image_array[tf.newaxis, ...])
    bestPredictionIndex = tf.argmax(prediction[0]).numpy()
    #compare bits to buttonMAp
    print(([buttonMap[labels[bestPredictionIndex] & x] for x in [1,2,4,8,16,32,64,128,256]]))
    print(labels[bestPredictionIndex])

print("start")
handle = getHandle('NullpoMino version7.6.0D')
while True:
    screenshot(handle)
    # print(prediction)

