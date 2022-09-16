  // this function is given 1 argument as string
  // we will have to write code that to do the following:
  // return a string containing all the characters that occur more than once
  // the order is determine by the frequency, following by alphabetical order if the number is the same
  // ex: string1 = "This is a sentence and an example"
  // output "eansit"
  // in the sentence above, "eansit" letters appear more than once
  // "i" and "t" both appear twice, but "i" is before "t" alphabetically
var test="This is a sentence and an example"
var test2="Here is another test so let us see if this works out"
var test1="This topic is moving along nicely and we are almost done with JavaScript"
function letFreqOrder(string1) {
    string = string1.toLowerCase().replace(/\s/g,'');
    counter={}

    //count all chars
    for(char of string){
        if(char in counter){
            counter[char]=counter[char]+1
        }
        else{
            counter[char]=1
        }
    }

    //remove char with <2 occurances
    for(char of Object.keys(counter)){
        if(counter[char]<2){
            delete counter[char]
        }
    }
    // Create items array
    var items = Object.keys(counter).map(function(key) {
        return [key, counter[key]];
    });
  
    // Sort the array based on the second element
    items.sort(function(first, second) {
        return second[1] - first[1];
    });
    //sort based on alpha
    items.sort(function(a,b){
        if(a[1]==b[1]){
            return a[0].charCodeAt(0)-b[0].charCodeAt(0)
        }
        else{
            return b[1]-a[1]
        }
    })
    var finalstring='';
    for(char of items){
        finalstring=finalstring+char[0]
    }
    return finalstring

}

console.log(letFreqOrder(test1))

module.exports = { letFreqOrder }
