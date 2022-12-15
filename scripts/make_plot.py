
import matplotlib.pyplot as plt
import src.data_generator as data_generator

x,y = data_generator.generatexy()

plt.plot(x,y,'r--')
plt.savefig("../docs/source/plots/red_line.png")
print("red fig saved")

plt.plot(x,y,'g--')
plt.savefig("../docs/source/plots/green_line.png")
print("green fig saved")

