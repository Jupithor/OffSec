function rules(array1,num1,string1){
    var array2=[]
    for(let x of array1){ 
        if(x.length == num1){
            array2.push(x)
        }
    }
    var firstword=array2[0]
    while(array2.includes(firstword)){
        array2[array2.indexOf(firstword)] = string1
    }
    
    newString1 = array2.join('');
    subString1 = newString1.substring(1,8);

    almosttherestring = subString1.split("").reverse().join('').toUpperCase()
    finalString = almosttherestring.substring(almosttherestring.length-3,almosttherestring.length)

    return finalString
}
