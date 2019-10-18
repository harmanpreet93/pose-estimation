This project aims at estimating a rough pose out of images. For the same, body joints are classified
such that each class represents a quadrant of 36 sized grid over the image. Connecting these joints gives
a rough estimation of pose.
	
### DATA FOLDER
- `images` - Contains resized images (150x150) from LSP dataset
- labels
	- Folder LSP contains original images and labels from LSP dataset.
	- A matlab script makeScaledLabels.m creates modified labels for the scaled images from original labels in `joints.mat`.
	- `joints_mod.mat` contains modified labels which are used for training and testing.


### `configuration.prototxt`
Contains the entire specification of the convolutional neural network according to the format
required by the caffe framework.
It also specifies the path of the training and test source files.
Network specification contains the convolutional layers and subsampling layers where each convolutional
layer contains the filter size and number of filters.


### `argument.prototxt`
This file contains various important parameters used for training.
- A path to the configuration file `configuration.prototxt` which specifies CNN architecture.
- Various other paramaters such as learning rate, momentum, iterations of test batches.
- Solver mode can be set to CPU or GPU.

### `train_data.txt` & `test_data.txt`
These files contain the absolute paths to the source images and their corresponding labels.
There are separate files for training data and test data.

### FINETUNING
Here is the data for Accuracy obtained over different configurations of CNNs.
For all the configurations, training `batchsize` is 10.

**`same momentum=0.9, same learning rate=0.0005`**
```
CN1(21*21*32)-P-CN2(16*16*64)-P-CN3(12*12*96)-F(1032) - max acc = 39 (features = 14)
CN1(21*21*32)-P-CN2(16*16*64)-P-CN3(12*12*96) - max acc = 41.333 (features = 14)
CN1(23*23*32)-P-CN2(19*19*64)-P-CN3(14*14*96) - max acc = 39.333 (features = 10)
CN1(21*21*32)-P-CN2(16*16*64)-P-CN3(12*12*96)-P - max acc = 42 (features = 10)
CN1(21*21*32)-P-CN2(16*16*64)-P-CN3(12*12*96)-P-CN4(5*5*96) - max acc = 42.677 (features = 3)
```

**Variations in learning rate, gamma**
```
CN1(21*21*32)-P-CN2(16*16*64)-P-CN3(12*12*96)-P-CN3(5*5*96) - max acc = 45.333 (features = 3) learning rate = .001
CN1(21*21*32)-P-CN2(16*16*64)-P-CN3(12*12*96)-P-CN3(5*5*96) - max acc = 42 (features = 3) learning rate = .001, gamma=0.005
```

**Variations in momentum**
```
CN1(23*23*32)-P-CN2(19*19*64)-P-CN3(14*14*96) - max acc = 33.333 (features = 10),momentum=0.6 (earlier it was 0.9)
CN1(23*23*32)-P-CN2(19*19*64)-P-CN3(14*14*96) - max acc = 41 (features = 10),momentum=0.9, learning rate = 0.0001
```
