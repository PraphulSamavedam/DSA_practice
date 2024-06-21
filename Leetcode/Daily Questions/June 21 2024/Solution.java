import Math;

class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int result = 0;
        int window = 0;
        int max_window = 0;
        int lt = 0;

        for (int rt=0; rt < customers.length; rt++){
            if (grumpy[rt] == 0){
                result += customers[rt];
            }
            else{
                window += customers[rt];
            }

            if (rt - lt + 1 > minutes){
                if(grumpy[lt] == 1){
                    window -= customers[lt];
                }
                lt += 1;
            }
            max_window = Math.max(max_window, window);
        }
        return max_window + result;
    }
}