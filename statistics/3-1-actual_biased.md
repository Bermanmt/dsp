[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

First we have the imports: 

	import chap01soln as ch
	import thinkstats2
	import thinkplot

We can read the data now: 

	resp = ch.ReadFemResp()

We build the first pmf: 
	
	pmf = thinkstats2.Pmf(resp.numkdh)
	
	Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})

