# In the real world, you would use much larger sets of data
# To create big data sets for testing, we use the Python module NumPy,
# which comes with a number of methods to create random data sets, of any size
import numpy
import matplotlib.pyplot as plt # to visualise the data set

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()