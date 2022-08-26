//Solutions to problems with hashmaps


//Solutuion for lc #136: single number
//checks if every element appears twice in a list
//outputs the one that appears once O(n) run time O(n) memory
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
// O(n) time  o(n) space complexity
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





//Solution for lc #1:Two Sum
//uses hash table too save all the numbers and then check for complement
// target-hash[nums[i]]; if complement exists return it
var twoSum  = function(nums,target){
    let vals = {};

    for (let i = 0; i < nums.length; i++) {
      if (target - nums[i] in vals) {
        
        return [vals[target-nums[i]], i];
        
      } else {
        vals[nums[i]] = i;
      }
    }
    return [];
}

list = [1,3,5,99,36];
console.log(twoSum(list,135))