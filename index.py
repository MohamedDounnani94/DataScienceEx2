import pandas as pd
import matplotlib.pyplot as plt

desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option("display.max_columns", 10)

titanic_csv = pd.read_csv('titanic.csv')

# GRAFICO CHE RAPPRESENTA LE ETA'
describe_ages = titanic_csv['Age'].describe()

print(describe_ages)

count_ages = titanic_csv['Age'].value_counts()
count_ages.sort_values()

count_ages.plot.bar()
plt.show()

