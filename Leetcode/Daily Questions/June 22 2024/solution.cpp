class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        /*
            Time Complexity: O(n)
            Space Complexity: O(1)
            Approach: Sliding Window
        */
        int result = 0;
        int lt = 0;
        int support = 1;
        int odd = 0;

        for (int rt = 0; rt < nums.size(); rt++){
            odd += nums[rt] % 2;

            if (odd == k){

                // Update the Support to make lt point at odd number
                if (!(nums[lt] % 2)){
                    support = 1;
                    while (!(nums[lt] % 2)){
                        support++;
                        lt++;
                    }
                }
            }

            else if (odd > k){

                // Move the lt pointer
                lt ++;
                odd--; // lt pointer always  pointed for odd number for odd == k

                // Update Support
                support = 1;
                while (!(nums[lt] % 2)){
                    support++;
                    lt ++;
                }

            }

            if (odd == k){
                result = result + support;
            }
        }
        return result;
    }
};