from scipy.stats import f_oneway

gp  = [23,21,25,30,28]
gp2 = [20,22,19,24,21]
gp3 = [18,20,22,19,21]

f_stat, p_val = f_oneway(gp, gp2, gp3)
print(f_stat, p_val)