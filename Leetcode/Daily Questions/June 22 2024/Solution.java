class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int odd = 0;
        int lt = 0;
        int result = 0;
        int support = 1;

        for (int rt=0; rt < nums.length; rt ++){
            odd += nums[rt] % 2;

            if (odd == k){
                // Update Support
                if (nums[lt] % 2 == 0){
                    support = 1;
                    while (nums[lt] % 2 == 0){
                        support++;
                        lt++;
                    }
                }
            }

            else if (odd > k){
                support = 1;
                // lt is pointing at odd number when odd == k
                odd--;
                lt++;

                // lt may not point at odd number any more
                while(nums[lt] % 2 == 0){
                    support ++;
                    lt++;
                }
            }

            // Update result
            if (odd == k){
                result = result + support;
            }
        }

        return result;
    }
}