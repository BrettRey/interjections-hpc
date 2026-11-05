# Is the 2-class LCA posterior log-odds exactly linear in M1's features (mean-imputed value + missingness indicator, with intercept)?
import numpy as np
rng=np.random.default_rng(1)
J,n=6,500
th1,th0=rng.uniform(.05,.95,J),rng.uniform(.05,.95,J); pi=.4
X=rng.integers(0,2,(n,J)).astype(float); M=rng.random((n,J))<.5
mu=rng.uniform(.2,.8,J)
L=np.log(pi/(1-pi))+np.where(M,0,X*np.log(th1/th0)+(1-X)*np.log((1-th1)/(1-th0))).sum(1)
Z=np.where(M,mu,X); F=np.c_[np.ones(n),Z,M.astype(float)]
coef,res,*_=np.linalg.lstsq(F,L,rcond=None)
print("max abs residual, unweighted:",np.abs(F@coef-L).max())
# with row-specific likelihood weights (testimony weighting), identity should fail
W=rng.uniform(.3,1,(n,J))
Lw=np.log(pi/(1-pi))+np.where(M,0,W*(X*np.log(th1/th0)+(1-X)*np.log((1-th1)/(1-th0)))).sum(1)
coef,*_=np.linalg.lstsq(F,Lw,rcond=None)
print("max abs residual, row-weighted:",np.abs(F@coef-Lw).max())
