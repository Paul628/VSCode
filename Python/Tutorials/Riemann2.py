def R(x,S,t):
 I=[0,0]
 while abs(S)>t:
    i=I[S>0]=I[S>0]+1
    if x(i)*S>0:S-=x(i)
    print(i)