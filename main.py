from numpy import genfromtxt
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

data = genfromtxt('/Users/admin/PycharmProjects/apstatsspringproject/Inflation vs 5-year treasury bond yields - Sheet1 (1).csv', delimiter=',')

years = data[:, 0]
inflation = data[:, 1]
yields = data[:, 2]
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
sns.scatterplot(yields, inflation)
slope, intercept, r_value, p_value, std_err = stats.linregress(yields, inflation)
plt.plot(yields, intercept + slope*yields, 'r', label='fitted line', linestyle=":")
plt.title("5-year Treasury Yields vs Inflation Scatter Plot")
plt.xlabel("5-year treasury yield")
plt.ylabel("Average Inflation")


plt.figure()
sns.residplot(yields, inflation)
plt.title("Residual Plot")
plt.ylabel("Residual for Predicted Value")
plt.xlabel("5-year treasury yields")

plt.figure()
sns.jointplot(yields, inflation, kind="reg")
plt.xlabel("5-year treasury yield")
plt.ylabel("Average Inflation")

print(f"intercept={intercept}")
print(f"p_value={p_value}")
print(f"r={r_value}")
print(f"slope={slope}")
print(f"standard error={std_err}")

plt.show()











