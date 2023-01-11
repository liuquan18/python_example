
import matplotlib.pyplot as plt
import src.data_generator as data_generator

plot_dir = "../docs/source/plots/"  # change here if path is not right


x,y = data_generator.generatexy()

# plot one
plt.plot(x,y,'r--')
plt.suptitle(plot_dir + "red line plot")
plt.savefig(plot_dir + "red_line.png")
print("red fig saved")

# plot two
plt.plot(x,y,'g--')
plt.suptitle("green line plot")
plt.savefig(plot_dir + "green_line.png")
print("green fig saved")

