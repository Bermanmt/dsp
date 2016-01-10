[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

First we have the imports: 

	import chap01soln as ch
	import thinkstats2
	import thinkplot

We can read the data now: 

	resp = ch.ReadFemResp()

We build the 'real' pmf and compute its mean: 
	
	pmf = thinkstats2.Pmf(resp.numkdh, label='real')
	pmf_mean = pmf.Mean()
	pritn pmf
	print('Real PMF Mean: ', pmf_mean)

	Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})

	Real PMF Mean:  1.0242

In order to build the 'observed' pmf we must first define the function that will calculate the BiasPmf:

	def BiasPmf(pmf, label=''):
		new_pmf = pmf.Copy(label=label)
		for x, p in pmf.Items():
			new_pmf.Mult(x,x)
		new_pmf.Normalize()
		return new_pmf


Now we can find de BiasPmf:

	bias_pmf= BiasPmf(pmf, label='bias')
	bias_pmf_mean=bias_pmf.Mean()

	print bias_pmf
	print 'Bias PMF Mean: ', bias_pmf_mean

	Pmf({0: 0.0, 1: 0.20899335717935616, 2: 0.38323965252938175, 3: 0.25523760858456823, 4: 0.10015329586101177, 5: 0.052376085845682166})

	Bias PMF Mean:  2.40367910066


If we plot both the Real PMF and the Biased PMF we will get something as follows:

	thinkplot.PrePlot(2)
	thinkplot.Pmf([pmf, bias_pmf])
	thinkplot.Show()

This results in: 

![Pmf_vs_Biased_pmf](https://github.com/Bermanmt/dsp/blob/master/statistics/img/biased_pmf.png)