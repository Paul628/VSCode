function spinWords(string){
    let reversestring = "";

    result = string.match(/("[^"]+"|[^"\s]+)/g);
     
    for(let i = 0; i < result.length; i++)
    {

        if (result[i].length >= 5)
        {
            
            for(let j = result[i].length-1; j >= 0; j-- )
            {
                reversestring += result[i][j];
            }
    
            result[i] = reversestring;             
        }

        if (i == result.length-1)
        {
            string += result[i];
        }
        else
        {
            string += result[i]+ " ";
        }  

        reversestring = "";
    }
  
    for(let i = 0; i < result.length; i++)
    {
           
        if (i == result.length-1)
        {
            reversestring += result[i];
        }
        else
        {
            reversestring += result[i]+ " ";
        }  
    }
    
    console.log(reversestring)

    return reversestring;
}

spinWords( "Hey fellow warriors" )