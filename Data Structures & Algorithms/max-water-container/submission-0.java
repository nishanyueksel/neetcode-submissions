class Solution {
    /*
    heights = [1,7,2,5,4,7,3,6]
    maintain two pointers
    l = 0, r = height.size()
    distance/width = height.size() - 0 = r - l
    height * width = 1 * 8 = 8
    make helper formula find area:
     min(left height, right height) * (indexOf(right) - indexOf(left))

    */
    public int maxArea(int[] heights) {
        int maximumArea = 0;
        int l = 0;
        int r = heights.length - 1;
        while (l < r) {
            int curr_height = findArea(l, r, heights);
            maximumArea = Math.max(maximumArea, curr_height);
            if (heights[l] < heights[r]) {
                l++;
            } 
            else {
                r--;
            }
        }
        return maximumArea;
    }
    public int findArea(int left_height_idx, int right_height_idx, int[] heights) {
        int height = Math.min(heights[left_height_idx], heights[right_height_idx]);
        int width = right_height_idx - left_height_idx;
        return height * width;
    }
}
