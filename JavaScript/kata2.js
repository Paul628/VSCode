function findOdd(A) 
{
    countappear(A);
    //console.log(A)
    return 0;
}

function countappear(A)
{
    var D = new Array(A.length).fill(0)
    //var C = [];
    let j = 0;
    console.log(D);
    
    for(i = 0; i < A.length; i++)
    {
        
        D[i][j] = A[i];
    }


    //console.log(j)
    console.log(A);
    console.log(D);
        
}


//findOdd([7]);                           //7
//findOdd([0]);                           //0
findOdd([1,1,2]);                       //2
//findOdd([1,2,2,3,3,3,4,3,3,3,2,2,1]);   //4