class Solution {
    public int[] twoSum(int[] nums, int target) {
      HashMap<Integer, Integer> maps = new HashMap<>();
        for (int i =0;i<nums.length;i++)
        {
            int num = nums[i];
            int diff = target - num;
            if (maps.containsKey(diff))
            {
                return new int[]{maps.get(diff),i};
            }
            maps.put(num,i);
        }
        return new int[]{};
    }
}
