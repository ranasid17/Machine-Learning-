import matplotlib.pyplot as plt 
import seaborn as sns

# Goal: Create and visualize PDF of twoDayChanges.py 
#   1) Must run twoDayChanges.py prior to this to create vars

# Run functions for twoDayChanges.py
a, b = getPrices(openPrices, closePrices)
c = relativeChange(a, b) 

# create PDF distribution
sns.distplot(c, hist=True, kde=True, bins=50, hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 1})
# modify plotting 
plt.ylabel('Observed Probability of Given Rel. Price Change') 
plt.xlabel('Observed 48h Relative Price Changes')
plt.title('48h Relative Price Changes of SPY, Oct 2019 - 2020')