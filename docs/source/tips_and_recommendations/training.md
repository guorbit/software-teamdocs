## Training and Testing Deep models

### Identifying common problems

In most cases it is recommended to use some sort of visualizer to monitor and log the models performance during training. 
There are many visualizers but my recommendation is to either use:
- Tensorboard, which comes built in with tensorflow, can be only accessed locally
- Weights and Biases, which is a third party tool that can be used with any framework, accessible from the browser

**Overfitting 📈:** Very common problem, where the model starts fitting the training data too well, and lacks generalization. Can be identified by looking at the training and validation loss, and seeing the validation loss increase while the training loss decreases.

**Underfitting 📉:** Another common problem, where the model is not complex enough to fit the data, or just the data has too much noise such the model can't generalise over it. Can be identified by having large errors on both the training and validation data.

**Vanishing gradient 👻:** A problem that occurs when the gradient of the loss function is too small, and the model can't learn. Can be identified by looking at the gradients of the model, and seeing them get smaller and smaller.

**Exploding gradient 🤯:** A problem that occurs when the gradient of the loss function is too large, and the model can't learn. Can be identified by looking at the gradients of the model, and seeing them get larger and larger.

### Selecting hyperparameters 🤔
Hyperparameters are the parameters of the model that are passed by the user such as batch size, learning rate, etc...
General rule of thumb:
- Set learning rate to 0.001
- Set batch size to the maximum that fits in memory
- Set number of epochs to 5-6 for fine tuning, 30-100 for training from scratch (depending on the size of the model and dataset)
- Set optimizer to Adam
- Set loss function to categorical crossentropy for classification, mean squared error for regression

It is also recommended to calculate accuracy during training and validation, however in case of generative image tasks this becomes expensive.

### Data augmentation ✨
Data augmentation is a technique used to increase the size of the dataset by applying transformations to the data, such as rotation, flipping, etc...
Many dataloader libraries have this built in, such as tensorflow, pytorch, and our utilities library.

### Transfer learning 🧠
Transfer learning is a technique used to use a model that was trained on a different task, and use it for a different task. This is done by removing the last layer of the model, and adding a new one, and training only the new layer. This is useful when the dataset is small, and the model is large, as it allows the model to learn from a larger dataset, and then fine tune it to the new task.

### Early stopping ⛔
Early stopping is a technique used to stop training when the model stops learning. This is done by monitoring the validation loss, and stopping when it stops decreasing. This is useful to prevent overfitting, and to save time.

### Model checkpointing 🚩
Model checkpointing is a technique used to save the model during training, so that it can be loaded later. This is useful to prevent losing progress.
