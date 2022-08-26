//Solutions to problems with hashmaps


//Solutuion for lc #136: single number
//checks if every element appears twice in a list
//outputs the one that appears once\
var singleNumber = function(nums) {
    let hashMap = {}
    
    for(let i of nums){
        if(!(i in hashMap)){
            hashMap[i] = i;
        }else{
            delete hashMap[i] ;
        }
    }return(Object.keys(hashMap)[0])
} 

let list = [1,3,3,4,5,5,4]

console.log(singleNumber(list))