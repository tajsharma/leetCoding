//lc #21: Merge Two sorted lists
//intialize dummy node for the head and current variable for tracking
//while loop to compare each item on the list; shifting pointers
//if lists have nodes to compare after; merge the remaining nodes
var mergeTwoLists = function(list1, list2) {
    var Dummy = {var:-1, next:  null};
    let current = Dummy;

    while(list1 && list2){
        if(list1.val < list2.val){
            current.next = list1;
            list1 = list1.next
        }else{
            current.next = list2;
            list2 = list2.next;
        }current = current.next;
    }
    current.next = list1 || list2;

    return Dummy.next;
};