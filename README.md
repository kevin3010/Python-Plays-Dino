# Python-Plays-Dino
Train Convolutional Neural networks to play chome's dinosaur game

MY WORKFLOW

Step-1 
Capture the data using 'capturing_data.py' file. This will separate the data into 'jump' and 'no' folder. From there the testing data need to be manually split into the testing and the training data.

Step-2
Create the numpy array using  'preaparing_data.py' which contains the image mapped with the label named after the folder in which the image was present.

Step-3 
Create the model and train the data and save the weights of the model for further use.

Step-4 
At the run-time capture the frames and pre-process the frame and feed that to the neural network and obtain the value of prediction and based on the value of prediction take the necessary action.
