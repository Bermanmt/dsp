[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

import thinkstats2
import thinkplot
from random import random


First we generate the 1000 random numbers:
	
		random_nums = [random() for i in range(0,1000)]


We can create both the PMF and the CDF:

		pmf = thinkstats2.Pmf(random_nums)
		cdf = thinkstats2.Cdf(random_nums)

Then we plot them:

		thinkplot.Pmf(pmf)
		thinkplot.Show(xlabel='Random Numbers', ylabel='Probability')

		thinkplot.Cdf(cdf)
		thinkplot.Show(xlabel='Random Numbers', ylabel='Probability')

In this case, since the random() function generates floats between 0 and 1 we will obtain a lot of random numbers whos probability of repeating themselves is close to none. Therefore, when we create the PMF we get as a result a lot of numbers who's probability is 1/1000 since they never repeat themselves. So the resulting graph looks something like this:

![pmf of random numbers](https://github.com/Bermanmt/dsp/blob/master/statistics/img/4.2-pmf1.png)

Once we plot the CDF we can see that the result is close to linear which tells us that the distribution is uniform:

![cdf of random numbers](https://github.com/Bermanmt/dsp/blob/master/statistics/img/4.2-CDF1.png)

To make this even more clear, we can generate an array of random integers between 0 and 1000 that will have a chance of repeating themselves:

	random_nums = [round(random()*1000) for i in range(0,1000)]

If we do the same procedure as shown above, we get the following plots. For the PMF:

![pmf of random numbers](https://github.com/Bermanmt/dsp/blob/master/statistics/img/4.2-pmf2.png)

![pmf of random numbers](https://github.com/Bermanmt/dsp/blob/master/statistics/img/4.2-cdf2.png)	


As it can be seen, we get a pmf in which we can have probabilities higher than 1/1000 and we still obtain a straight line when whe plot the CDF which tells us that the distribution is uniform too. 


