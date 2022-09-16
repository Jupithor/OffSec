    // this function is given 1 argument as string
    // we will have to write code to do the following:
    // count all the vowels that show up more than once
    // return an array of objects containing vowels (in alphabetic order) and number of occurrence
    // ex: string1 = "iighjleldlfelqwpeghnoxcvoa"
    // output: [{"e":3}, {"i":2}, {"o":2}]
    // only consider the letters: a,e,i,o,u (not y)
    // do not include vowels if they do not occur more than once
function countDuplicateVowels(string1) {
    vowels=['a','e','i','o','u']
    var counter = new Object();
    var counter = {};
    var output = []
    for (letter of string1){
        if (vowels.includes(letter)){
            if(letter in counter){
                counter[letter]=counter[letter]+1}
            else{
                counter[letter]=1
            }
        }
    }
    sorted=Object.keys(counter).sort().reduce((r,k) => (r[k] = counter[k],r),{})

    for([k,v] of Object.entries(sorted)){
        if (v>1){
            output.push("\""+k+"\":"+v)
        }
    }
    
  }
countDuplicateVowels("iighjleldlfelqwpeghnoxcvoa")

  
  module.exports = { countDuplicateVowels }
  