from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import cPickle as pickle
import numpy as np
import sys


data = SupervisedDataSet(3, 1)

data.addSample([0,0,0],[0])
data.addSample([0,0,1],[1])
data.addSample([0,1,0],[1])
data.addSample([0,1,1],[0])
data.addSample([1,0,0],[1])
data.addSample([1,0,1],[0])
data.addSample([1,1,0],[0])
data.addSample([1,1,1],[1])


if sys.argv[1] == "train":
	print(sys.argv[2])

	net1 = buildNetwork(data.indim, 3 , data.outdim)
	trainer1 = BackpropTrainer(net1, dataset = data, verbose=True)
	for i in xrange(int(sys.argv[2])):
	    trainer1.trainEpochs(1)
	    print('\tValue after %d epochs: %.2f'%(i, net1.activate([sys.argv[3],sys.argv[4],sys.argv[5]])[0]))
	pickle.dump(net1, open('testNetwork.dump', 'w'))
if len(sys.argv) == 4:
	net1 = pickle.load(open('testNetwork.dump'))
	trainer1 = BackpropTrainer(net1, dataset=data, verbose=True)
	trainer1.trainEpochs(1)
	print('Value: %.2f'%(net1.activate([sys.argv[1],sys.argv[2],sys.argv[3]])[0]))