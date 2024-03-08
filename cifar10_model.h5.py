
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# Загрузка и предварительная обработка данных
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Нормализация данных
train_images, test_images = train_images / 255.0, test_images / 255.0

# Создание модели
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

# Компиляция модели
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Обучение модели
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

# Оценка модели
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nТочность на тестовом наборе данных:', test_acc)

# Визуализация результатов обучения (по желанию)
plt.plot(history.history['accuracy'], label='Точность на обучающем наборе')
plt.plot(history.history['val_accuracy'], label = 'Точность на валидационном наборе')
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.ylim([0, 1])
plt.legend(loc='lower right')
model.save('cifar10_model.h5')
