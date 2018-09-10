import numpy as numpy
import matplotlib.pyplot as mathplot
import pandas as pandas

# Compute the x and y coordinates for points on a sine curve
x = numpy.arange(0, 3 * numpy.pi, 0.1)
y = numpy.sin(x)
mathplot.title("sine wave form")

# Plot the points using matplotlib
mathplot.plot(x, y)
mathplot.show()

#random scatter
df = pandas.DataFrame(numpy.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')
mathplot.title("random scatter")
mathplot.show()

#Line chart
x = numpy.arange(0, 10)
y = x ^ 2
#Labeling the Axes and Title
mathplot.title("Graph Drawing")
mathplot.xlabel("Time")
mathplot.ylabel("Distance")

# Formatting the line colors
mathplot.plot(x, y, 'r')

# Formatting the line type
mathplot.plot(x, y, '>')
mathplot.show()

