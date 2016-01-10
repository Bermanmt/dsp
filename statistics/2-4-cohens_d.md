[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

The effect size when we compare pregnancy lengths between first borns and others is 0.029 which means that the difference in means between these to groups is approximately 0.029 Standard Deviations.

When we comparte the weight in Oz between first borns and others, we obtain a Cohen's D value of -0.089 which means that first babies are approximately 0.089 standard deviations lighter than others. 

From these results, we can observe that the difference between  first born's and other's weights are much higher than when we compare them with pregnancy lengths. However, both deferences are not significant when placed in context since the difference is really small and doesn't appear to have any practival consequences. 


Code Used: 

import nsfg
import thinkstats2
import thinkplot

df = nsfg.ReadFemPreg()
df = CleanFemPreg(df)

live = df[df.outcome==1]

firsts= live[live.birthord==1]
others = live[live.birthord!=1]

prglngthEffect = thinkstats2.CohenEffectSize(firsts.prglngth,others.prglngth)
totalwgtEffect = thinkstats2.CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb)

