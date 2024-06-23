class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        /*
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        Approach: Two priority queue based solution
        */
        int lt = 0;
        int result = 0;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;

        priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> maxHeap;

        for (int rt = 0; rt < nums.size(); rt ++){

            minHeap.push(make_pair(nums[rt], rt));
            maxHeap.push(make_pair(nums[rt], rt));

            while (maxHeap.top().first - minHeap.top().first > limit){
                lt = min(minHeap.top().second, maxHeap.top().second) + 1;

                while (minHeap.top().second < lt){
                    minHeap.pop();
                }

                while (maxHeap.top().second < lt){
                    maxHeap.pop();
                }
            }

            result = std::max(result, rt - lt + 1);
        }

    return result;
    }
};