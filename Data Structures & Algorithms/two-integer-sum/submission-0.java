class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> sol_map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (sol_map.containsKey(complement)) {
                return new int[] {sol_map.get(complement), i};
            }
            sol_map.put(nums[i], i);
        }
        return new int[] {};
    }
}
