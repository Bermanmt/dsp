[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

We can modify the Estimate3() function in the estimation.py file in order to get the requested values:

	import thinkstats2
	import estimation
	import numpy as np
	import math
	import thinkplot


	def EstimateExp(n=10, m=1000, lam=2):
		lam = lam

		means=[]
		medians=[]
		for _ in range(m):
			xs = np.random.exponential(1.0/lam, n)
        	L = 1 / np.mean(xs)
        	Lm = math.log(2) / thinkstats2.Median(xs)
       		means.append(L)
        	medians.append(Lm)
		cdf = thinkstats2.Cdf(means)
		ci = (cdf.Percentile(5), cdf.Percentile(95))
		stderr =  estimation.RMSE(means,lam)       

        print n, stderr, ci 


Now we can make several calls on the function and see what happens as m increases:

	EstimateExp(n=10, m=1000, lam=2)
	EstimateExp(n=50, m=1000, lam=2)
	EstimateExp(n=100, m=1000, lam=2)
	EstimateExp(n=500, m=1000, lam=2)
	EstimateExp(n=1000, m=1000, lam=2)

	10   0.799502103482  (1.2943814230447843, 3.6027034061272083)
	50   0.297997162768  (1.5987407978945556, 2.5710244091893673)
	100  0.207451081679  (1.7143181632904136, 2.3769349469240937)
	500  0.0885161984043 (1.8583003858446832, 2.150336396974514)
	1000 0.0647179295028 (1.9034351348238152, 2.1163062761372928)


As the sample size (n) increases, the standard error decreases and the amplitude of the Confidence intervale decreases too.

	def EstimateExp(n=10, m=1000, lam=2):
		lam = lam
		means=[]
		medians=[]
		for _ in range(m):
			xs = np.random.exponential(1.0/lam, n)
			L = 1 / np.mean(xs)
			Lm = math.log(2) / thinkstats2.Median(xs)
			means.append(L)
			medians.append(Lm)
		cdf = thinkstats2.Cdf(means)
		ci = (cdf.Percentile(5), cdf.Percentile(95))
		stderr =  estimation.RMSE(means,lam)
		return (n, stderr) 

	pairs = []
	for i in range(10,1000,40):
		pairs.append(EstimateExp(n=i))

	thinkplot.Plot(*zip(*pairs))
	thinkplot.Show(xlabel='Sample Size (n)', ylabel='Standard Error')

Here we can see the graph of Samplse Size vs Standard Error: 

![Sample Size vs Std Error](https://github.com/Bermanmt/dsp/blob/master/statistics/img/8.2-Stderr.png)

