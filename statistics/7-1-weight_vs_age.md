[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

Wwe make an initial approach to the problem by plotting a graph of mother's age vs baby's weight:

	import thinkstats2
	import thinkplot
	import nsfg
	import numpy as np

	data = nsfg.ReadFemPreg()
	live = data[data.outcome==1]
	live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
	motherage = live.agepreg
	weight = live.totalwgt_lb
	thinkplot.Scatter(motherage, weight)
	thinkplot.Show(xlabel='Mother Age', ylabel='Weight')

This results in a scatter plot as shown:

![Age vs. Weight](https://github.com/Bermanmt/dsp/blob/master/statistics/img/7.1-agevsweight.png)

In order to plot percentiles of birth weight versus mother's age we have to do the foloowing: 

	bins = np.arange(10, 50,5)
	indices = np.digitize(motherage, bins)
	groups = live.groupby(indices)
	ages = [group.agepreg.mean() for i, group in groups]
	cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i,group in groups]

	for percent in [75, 50, 25]:
		weights = [cdf.Percentile(percent) for cdf in cdfs]
		label = '%dth' %percent
		thinkplot.Plot(ages, weights, label=label)

	thinkplot.Show()

We obtain the graph:

![Age vs. Weight probability](https://github.com/Bermanmt/dsp/blob/master/statistics/img/7.1-agevsweightpercentage.png)

Now we compute the correlations: 
	
		pearsons = thinkstats2.Corr(motherage,weight)

		Pearsons Correlation:  0.0688339703541

		spearman = thinkstats2.SpearmanCorr(motherage,weight)

		Spearmans Correlation:  0.0946100410966

From the first plot we can see that there is no clear correlation between the datasets. Once we plto the second graph with the percentiles, we can observe that the variables have no direct linear correlation. In fact if you observe the graph for the 25th percentile, you'll be able to see that in fact the relationship between the variables doesn't seem to follow a clear pattern. 

When we compute Pearson's Correlation and Spearman's correlation, what we saw in the graphs is confirmed, since we find two values really close to 0 that indicates that any correlation between these variables is really weak. 
