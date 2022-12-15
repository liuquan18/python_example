#%matplotlib inline

import matplotlib.pyplot as plt
import src.data_generator as data_generator

x,y = data_generator.generatexy()

print(x)
print(y)

# plt.savefig("../docs/source/plots/example.png")
# print("fig saved")