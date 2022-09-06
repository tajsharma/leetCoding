// lc # 169: majority element 
//algo uses 2 for loops; first to create map object of each key
// 2nd loop increments the count each time the same # is seeen
//returns the highest count in the map;
var majorityElement = function(nums){
    let map = {};
    for(let i=0; i<nums.length; i++){
        if(!(map[i])){
            map[nums[i]] = 0;
        }
    }
    for(let j=0; j<nums.length; j++){
        map[nums[j]] +=1;
    }
    let arr = (Object.values(map));
    let highestCount = Math.max(...arr);
    return Object.keys(map).find(key=>map[key] ===highestCount);
};

//simpler solution to problem above
//returns the element that exists more than n/2 times 
var majorityElement2 = function(nums) {
    var obj = {};
    
    for(var i = 0; i < nums.length; i++){
        obj[nums[i]] = obj[nums[i]] + 1 || 0; //the || initializes each value to 0;
        console.log(obj)
        if(obj[nums[i]] > ((nums.length / 2)-1))  return nums[i];
    }
    
};

let arr = [2,3,4,3,3,2,3];
console.log(majorityElement2(arr))









