import nsfg
import thinkstats2
import thinkplot

df = nsfg.ReadFemPreg()
df = CleanFemPreg(df)

live = df[df.outcome==1]

firsts= live[live.birthord==1]
others = live[live.birthord!=1]

def ReadFemResp(dct_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz'):
	dct=thinkstats2.ReadStataDct(dct_file)
	df=dct.ReadFixedWidth(dat_file,compression='gzip')
	return df