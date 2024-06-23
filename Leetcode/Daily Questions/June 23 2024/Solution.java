class Solution {
    /*
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    Approach: Two Queue Approach
    */
    public int longestSubarray(int[] nums, int limit) {
        int lt = 0;
        int result = 0;
        int n = nums.length;
        PriorityQueue<Pair<Integer, Integer>> minHeap = new PriorityQueue<Pair<Integer, Integer>>(n, (a, b) -> a.getKey() - b.getKey());

        PriorityQueue<Pair<Integer, Integer>> maxHeap = new PriorityQueue<Pair<Integer, Integer>>(n, (a, b) -> b.getKey() - a.getKey());
        for (int rt =0; rt < nums.length ; rt ++){
            minHeap.add(new Pair<Integer, Integer>(nums[rt], rt));
            maxHeap.add(new Pair<Integer, Integer>(nums[rt], rt));

            if (maxHeap.peek().getKey() - minHeap.peek().getKey() > limit) {

                lt = Math.min(maxHeap.peek().getValue(), minHeap.peek().getValue()) + 1;

                while (maxHeap.peek().getValue() < lt) {
                    maxHeap.remove();
                }

                while (minHeap.peek().getValue() < lt ){
                    minHeap.remove();
                }

            }

            result = Math.max(result, rt - lt + 1);
        }

        return result;
    }
}