[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

According to the sample, the first thing we are going to need is to read the data and then run the InterpolateSample function from the hinc2.py file: 

	import thinkstats2
	import thinkplot
	import hinc
	import hinc2

	df=hinc.ReadData()
	log_sample=hinc2.InterpolateSample(df)
	log_cdf=thinkstats2.Cdf(log_sample)

First, lets plot the data to be able to see how it looks:

	pdf = thinkstats2.EstimatedPdf(log_sample)
	thinkplot.Pdf(pdf, label='Household Income')
	thinkplot.Show()


If we take a close look it seems like the distribution is skewed to the left:

![Income Distribution](https://github.com/Bermanmt/dsp/blob/master/statistics/img/6.1-IncomeDist)

Now lets calculate the different statistics:

	log_mean=log_cdf.Mean()
	mean = 10**log_mean
	log_median=log_cdf.Value(0.5)
	median = 10**log_median
	skewness=thinkstats2.Skewness(log_sample)
	pearson_skewness=thinkstats2.PearsonMedianSkewness(log_sample) 

These are the results:

	Mean: 45455.4263813
	Median:  51226.4544789
	Skewness:  -0.641354366566
	Pearson Skewness:  -0.337920251338

To get the the percentage of people with a taxable income below the mean: 
	
	below_mean = log_cdf[log_mean]

	Below income: 0.45

Which means approximately 45% of the people are located below the mean.
