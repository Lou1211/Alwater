import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import csv

ncols = 302
nrows = 262
nasc = 41

need = input()
need = int(need)

Fset = []
i=0;

#Data in
input = pd.read_csv('dm1d0000.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0001.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0002.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0003.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0004.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0005.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0006.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0007.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0008.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0009.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0010.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0011.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0012.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0013.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0014.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0015.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0016.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0017.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0018.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0019.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0020.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0021.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0022.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0023.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0024.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0025.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0026.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0027.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0028.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0029.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0030.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0031.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0032.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0033.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0034.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0035.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0036.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0037.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0038.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0039.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0040.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

input = pd.read_csv('dm1d0041.asc', skiprows=6, sep=' ', skipinitialspace=True)
input.to_csv("try.csv", index=False, sep=',')
test = pd.read_csv('try.csv', sep=',', skipinitialspace=True, header=None, index_col=False)
set = test.iloc[1:nrows, 1:ncols].values
tmp = set[int(need/ncols)][int(need % ncols)]
Fset.append(float(tmp))

#plot
plt.plot(Fset, color='red')
plt.savefig('When position data is '+str(need)+'.jpg')
plt.show()