# This script generates text files containing path to the images with their labels

import scipy.io
import math

# path to the project root
pathPrefix = '/home/chinmay/Desktop/ML Project/'

mat = scipy.io.loadmat(pathPrefix + 'data/labels/joints_mod.mat')
joints = mat['joints_mod']

num_train = 1000
num_test = 100

# path to the images folder
imagePath = pathPrefix + 'data/images/'

# joint number for which labels are required
joint_number = 5

# training data file
fileContents = ''
for i in range(0,num_train):
	coords = joints[0:2,joint_number-1,i]
	col = math.ceil(float(coords[0])/25)
	row = math.ceil(float(coords[1])/25)
	label = 6*(row-1) + col
	fileContents+=imagePath+str(i+1)+'.jpg' + '\t' + str(int(label)) + '\n'
text_file = open('train_data.txt','w')
text_file.write(fileContents)
text_file.close()

# test data file
fileContents = ''
for i in range(num_train,num_train+num_test):
	coords = joints[0:2,joint_number-1,i]
	col = math.ceil(float(coords[0])/25)
	row = math.ceil(float(coords[1])/25)
	label = 6*(row-1) + col
	fileContents+=imagePath+str(i+1)+'.jpg' + '\t' + str(int(label)) + '\n'
text_file = open('test_data.txt','w')
text_file.write(fileContents)
text_file.close()