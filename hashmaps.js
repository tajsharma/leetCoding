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
//let list = [1,3,3,4,5,5,4]
//console.log(singleNumber(list))




//Solution for lc #217: contains duplicate
//checks if an array of numbers contains a duplicate
var containsDuplicate = function(nums){
    let hash = {};

    for(let i =0; i <nums.length; i++){
        if(hash[nums[i]]){
            return true;
        }else{
            hash[nums[i]]=true;
        }
    }return  false;
}

//let nums1= [1,2,3,4,5];
//console.log(containsDuplicate(nums1))


