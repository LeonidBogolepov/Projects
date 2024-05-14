import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2


#1.Предобученная нейронка
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

#2.Подготовка и загрузка изображения
def loadimage(img_path):
  img = tf.io.read_file(img_path)
  img = tf.image.decode_image(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)
  img = img[tf.newaxis, :]
  return img

content_image = loadimage('Image/Abrams_X.jpg')
style_image = loadimage('Image/photo_2024-05-06_15-35-39.jpg')

#3. Орисовка изображения

plt.imshow(np.squeeze(content_image))
plt.show()
plt.imshow(np.squeeze(style_image))
plt.show()

#4. Стилизация изображения
stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
plt.imshow(np.squeeze(stylized_image))
plt.show()

#4. Вывод готового изображения
cv2.imwrite('Image/generated_img.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))
