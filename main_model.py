# -*- coding: utf-8 -*-
"""main_model.py

Automatically generated by Colaboratory.

"""

# A Fourier-transformed feature engineering design for predicting ternary perovskite properties by coupling a two-dimensional convolutional neural network 
# with a support vector machine (Conv2D-SVM)

# AUTHOR - (1) * Ericsson Chenebuah, (1) Michel Nganbe and (2) Alain Tchagang 
# 1: Department of Mechanical Engineering, University of Ottawa, 75 Laurier Ave. East, Ottawa, ON, K1N 6N5 Canada
# 2: Digital Technologies Research Centre, National Research Council of Canada, 1200 Montréal Road, Ottawa, ON, K1A 0R6 Canada
# * email: echen013@uottawa.ca 
# (06-Dec-2022)


## THIS SOURCE CODE PERFORMS THE PREDICTION EXERCISE ON A CONVOLUTIONAL NEURAL NETWORK COUPLED WITH THE SUPPORT VECTOR MODEL

# Load the previosuly developed high-dimensional input image from the python file [input_img.py]

data_size = 27587
_input_img = _input_img.reshape(data_size,154,60,1)

# Load the target prediction property file. 
# The column headers "delta_e", "band_gap" and "stability" stands for the formation energy, energy band gap, and stability energy, respectively.
df = pd.read_csv('target.csv')

# The code is simulated on formation energy (delta_e) prediction. For a different target property, modify the code using the predefined column header.
y = np.asarray(df['delta_e'].astype('float32'))

# Split data into train, test and validation sets
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(_input_img, y, test_size=0.2, random_state=72)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.25, random_state=0)


# CONVOLUTIONAL NEURAL NETWORK ARCHITECTURE
import keras
from keras import layers
from tensorflow.keras.optimizers import Adam

input_img = keras.Input(shape=(154, 60, 1))

x = layers.Conv2D(8, kernel_size=(3, 3), activation='relu')(input_img)
x = layers.Conv2D(16, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Dropout(0.2)(x)

x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(16, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Dropout(0.2)(x)

x = layers.Conv2D(4, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(2, (3, 3), activation='relu', padding='same')(x)
x = layers.Flatten()(x)

x = layers.Dense(570, activation='relu')(x)
x = layers.Dense(285, activation='relu')(x)


feat_ext = layers.Dense(10, activation='tanh')(x) #Feature extraction layer
target = layers.Dense(1, activation='linear')(feat_ext)
    
opt = Adam(learning_rate=1e-4, decay=1e-3/200) 
model = keras.Model(input_img, target)
encoder = keras.Model(input_img, feat_ext, name="encoder") # Encoded feature extracted layer

model.compile(loss="mean_squared_error", optimizer=opt, metrics=['mae'])
history = model.fit(X_train, y_train, epochs=500, validation_data=(X_val, y_val))

# Plot the learning curves on the Conv2D (pre-training) history to inspect the challenge of over-fitting
%matplotlib inline 
import matplotlib.pyplot as plt

accuracy = history.history['mae']
val_accuracy = history.history['val_mae']

loss = history.history['loss'] #MSE
loss = (np.array(loss))**0.5 #RMSE
val_loss = history.history['val_loss'] #MSE
val_loss = (np.array(val_loss))**0.5 #RMSE

epochs = range(len(accuracy))

plt.plot(epochs, accuracy, 'b', label='Training accuracy')
plt.plot(epochs, val_accuracy, 'r', label='Validation accuracy')
plt.xlabel('Epoch', fontsize=20, fontweight='bold')
plt.ylabel('MAE', fontsize=20, fontweight='bold')
plt.legend(fontsize=15)
plt.grid()
plt.xscale('log')
plt.figure()

plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.xlabel('Epoch', fontsize=20, fontweight='bold')
plt.ylabel('RMSE', fontsize=20, fontweight='bold')
plt.legend(fontsize=15)
plt.grid()
plt.xscale('log')
plt.show()

# Evaluate the prediction accuracy of the pre-training exercise using standardized metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

y_val_pred = model.predict(X_val)

print("MSE val: %.4f"% mean_squared_error(y_val, y_val_pred))
print("RMSE val: %.4f" % np.sqrt(mean_squared_error(y_val, y_val_pred)))
print('R-square val: %.4f' % r2_score(y_val, y_val_pred))
print("MAE val: %.4f"% mean_absolute_error(y_val, y_val_pred))

print("__________________________________________________________________")

y_pred = model.predict(X_test)

print("MSE test: %.4f"% mean_squared_error(y_test, y_pred))
print("RMSE test: %.4f" % np.sqrt(mean_squared_error(y_test, y_pred)))
print('R-square test: %.4f' % r2_score(y_test, y_pred))
print("MAE test: %.4f"% mean_absolute_error(y_test, y_pred))


# Plot regression fitting based on predicted vs actual
from scipy.stats import gaussian_kde
xy = np.vstack([y_test, y_pred.reshape(5518,)])
z = gaussian_kde(xy)(xy)
fig = plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, c=z, s=5)
plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')
plt.colorbar().ax.tick_params(labelsize=15)
plt.xlabel('Actual', fontsize=20, fontweight='bold')
plt.ylabel('Predicted', fontsize=20, fontweight='bold')

plt.show()


# Extract the high-quality features from the feature-extraction layer and couple with the SVM model for final training
_x = encoder.predict(_input_img) 

# Uncomment line below if you wish to save the trained parameters (weights) of the feature extracted layer
# encoder.save('encoder_enc.h5')

from sklearn.svm import SVR
from sklearn.model_selection import cross_validate

regr=SVR(kernel='rbf', degree=3, gamma='scale', coef0=0.0, tol=0.001, C=1.0, epsilon=0.1)

scoring = ["neg_mean_absolute_error", "neg_mean_squared_error", "r2"]
scores = cross_validate(regr, _x, y, cv=5, scoring=scoring)

# Evaluate final trained version

print("avg mae: ", np.mean(scores['test_neg_mean_absolute_error']))
print("std mae: ", np.std(scores['test_neg_mean_absolute_error']))

print("avg mse: ", np.mean(scores['test_neg_mean_squared_error']))
print("std mse: ", np.std(scores['test_neg_mean_squared_error']))

print("avg r2: ", np.mean(scores['test_r2']))
print("std r2: ", np.std(scores['test_r2']))
