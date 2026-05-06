class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */

    /*
    numbers = [1,2,3,4], target = 3
    numbers[0] = 1 = l
    numbers[3] = 4 = r
    1+4 > 3 so  move r down
    1 + 3 >3 so move r down
    1+2 === 3 so return l + 1, r+1
    

    */
    twoSum(numbers, target) {
        let l = 0, r = numbers.length - 1;
        while (l < r) {
            if (numbers[l] + numbers[r] > target) {
                r--;
            }
            else if (numbers[l]+ numbers[r] < target) {
                l++;
            }
            else {
                return [l+1, r+1]
            };
        };
    };
};
