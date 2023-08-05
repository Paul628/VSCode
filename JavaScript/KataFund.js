function countBy(x, n) {
    let z = new Array(n)
    for (i=0; i<n; i++)
    {
        z[i]=x*(i+1)        
    }
    
    console.log(z);
    return z;
  }




countBy(1, 10)
countBy(2, 5)