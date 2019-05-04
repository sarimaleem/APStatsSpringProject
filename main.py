#MR MEYER READ THIS IF YOU ARE LOOKING AT MY CODE
#THIS IS MY RAW CODE, ITS DIFFICULT TO UNDERSTAND ANYTING FROM IT
#I'VE CREATED A NICE VISUALIZATION CLICK ON THE LINK BELOW
#    https://www.kaggle.com/explodingmind/test-kernel?scriptVersionId=13721952


from numpy import genfromtxt
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

data = genfromtxt('/Users/admin/PycharmProjects/apstatsspringproject/Inflation vs 5-year treasury bond yields - Sheet1 (1).csv', delimiter=',')

years = data[:, 0]
inflation = data[:, 1] * 100
yields = data[:, 2]

testHue = []

for i in range(7):
    testHue.append("1960s")

for i in range(10):
    testHue.append("1970s")

for i in range(10):
    testHue.append("1980s")

for i in range(10):
    testHue.append("1990s")

for i in range(10):
    testHue.append("2000s")

for i in range(9):
    testHue.append("2010s")




sns.set(style="darkgrid")


#inflation plot
sns.lineplot(years, inflation)
plt.xlabel("Time (years)")
plt.ylabel("Average Inflation")
plt.title("Inflation over Time")

plt.figure()
sns.lineplot(years, yields)
plt.xlabel("Time (years)")
plt.ylabel("5-year treasury yields")
plt.title("5-year treasury yields over time")

plt.figure()
sns.scatterplot(inflation, yields, hue=testHue)
slope, intercept, r_value, p_value, std_err = stats.linregress(inflation, yields)
plt.plot(yields, intercept + slope*yields, 'r', label='fitted line', linestyle=":")
plt.title("5-year Treasury Yields vs Inflation Scatter Plot")
plt.ylabel("5-year treasury yield (Percentage Points)")
plt.xlabel("Average Annual Inflation (Percentage Points)")

plt.figure()
sns.residplot(inflation, yields)
plt.title("Residual Plot")
plt.ylabel("Residual for Predicted Value")
plt.xlabel("Inflation (Percentage Points)")

residuals = []

for i in range(np.prod(inflation.shape)):
    x = inflation[i]
    pred = x * slope + intercept
    obs = yields[i]
    resid = obs - pred
    residuals.append(resid)

plt.figure()
npp = stats.probplot(residuals, plot=plt)
plt.title("Normal Probability Plot for Residuals")
plt.ylabel("Observed Residual")
plt.xlabel("Expected Normal Residual")


plt.figure()
sns.jointplot(inflation, yields, kind="reg")
plt.xlabel("5-year treasury yield (Percentage Points)")
plt.ylabel("Average Annual Inflation (Percentage Points)")

print(f"intercept={intercept}")
print(f"p_value={p_value}")
print(f"r={r_value}")
print(f"slope={slope}")
print(f"standard error={std_err}")

plt.show()











