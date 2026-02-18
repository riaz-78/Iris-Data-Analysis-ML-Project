#importing libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading Iris dataset using 
iris = pd.read_csv("iris.csv")

#Displaying dataset using .shape, .columns and .head()
print(iris.shape)
print(iris.columns)
print(iris.head())
print (iris.info())
print(iris.describe())

                          #   ====>>> basic data visualization using matplotlib and seaborn  <<<====

# Scatter plot for analyzing relationships b/w variables

sns.scatterplot(
    data=iris,
    x="petal_length",
    y="petal_width",
    hue="species"
)
plt.title("Scatter Plot: Petal Length vs Petal Width")
plt.xlabel("Petal Length")
plt.xlabel("Petal Width")

plt.show()

# Examining data distribution using Histogram.

plt.hist(iris["sepal_length"],bins=20)

plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")

plt.show()

# Detecting outliers and spread of values using Box plot

sns.boxplot(
    data=iris,
    x="petal_length",
    y="petal_width",
    hue="species"
)
plt.title("Box Plot: Petal Length vs Petal Width")
# plt.xlabel("Petal Length")
# plt.xlabel("Petal Width")

plt.show()

