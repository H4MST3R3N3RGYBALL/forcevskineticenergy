import pandas as pd
import matplotlib.pyplot as plt
import math
import decimal
import random
import numpy as np
from scipy.interpolate import spline
#naming format:
#Files must be in order starting at lowest grams and then go up in order
#Name of file must be <NUMBER OF GRAMS>gt<TRIAL NUMBER> ex 200gt1, 200gt2, 200gt3
files = ['200gt1', '200gt2', '200gt3', '300gt1', '300gt2', '300gt3', '400gt1', '400gt2', '400gt3', '500gt1', '500gt2', '500gt3', '600gt1', '600gt2', '600gt3']

#Removes stuff such as negetives and invalid pieces of data
def negHandler(templist):
	l1 = []
	l2 = []
	finallist = []
	for x in templist:
		l1.append(x[0])

	for y in l1:
		if str(y) != 'nan' and float(y) > 0:
			finallist.append(y)

	return finallist

def findMass(nameOfFile):
	m1 = nameOfFile.replace("g", "")
	m2 = m1.replace("t1", "")
	m2 = m2.replace("t2", "")
	m2 = m2.replace("t3", "")
	return float((float(m2) * 0.001))

def findChangeInX(inputList):
	currentMin = 10.0
	currentMax = 0.0
	for counter in inputList:
		if float(counter) > currentMax:
			currentMax = float(counter)

		elif float(counter) < currentMin:
			currentMin = float(counter)
	changeInX = (currentMax - currentMin)
	return changeInX

def turnDataFrameIntoList(nameOfFile):
	nameOfFile = nameOfFile + '.csv'

	data = pd.read_csv(nameOfFile)
	df = pd.DataFrame(data, columns=['Trial'])
	l = df.values.tolist()
	return l

def fTension(changeinx):
	return(25 * changeinx)

def fNetY(ftension, mass):
	fG = (-9.81 * mass)
	fNetYl = (ftension - fG)
	return fNetYl

def kineticEnergy(dX, m1):
	p1 = float(9.81 * m1 * dX)
	p2 = float(0.5 * 25 * (dX ** 2))
	finalKe = float(p1 - p2)

	return finalKe

def modular():
	counter = 0
	xcords = []
	ycords = []

	for x in range(<INSERT NUMBER OF UNIQUE MASSES>):
		sumOfKe = 0
		sumOfForce = 0
		for y in range(<INSERT NUMBER OF TRIALS HERE it must be constant with all other sets of data>):
			dm = turnDataFrameIntoList(files[counter])
			fList = negHandler(dm)

			mass = findMass(files[counter])

			deltaX = findChangeInX(fList)

			force = fNetY(fTension(deltaX), mass)

			ke = kineticEnergy(deltaX, mass)

			sumOfForce = sumOfForce + force
			sumOfKe = sumOfKe + ke

			counter += 1

		xcords.append(sumOfForce)
		ycords.append(sumOfKe)

	plt.ylabel('Final Kinetic Energy: (J)')
	plt.xlabel('Net Force: N')

	x2_axis = np.array(xcords)
	y2_axis = np.array(ycords)

	#x_new = np.linspace(x2_axis.min(), x2_axis.max(), 500)
	#power_smooth = spline(x2_axis, y2_axis, x_new)

	#plt.plot(x_new, power_smooth, marker='o')
	plt.plot(xcords, ycords, marker='o')

	plt.show()

	for mmmmmmm in range(5):
		print(xcords[mmmmmmm], ycords[mmmmmmm])
		
modular()



		























