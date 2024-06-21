class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int result = 0;
        int window = 0;
        int max_window = 0;
        int lt = 0;

        for(int rt=0; rt < customers.size(); rt ++){
            if (grumpy[rt] == 1){
                window += customers[rt];
            }
            else{
                result += customers[rt];
            }

            if (rt - lt + 1 > minutes){
                if (grumpy[lt]){
                    window -= customers[lt];
                }
                lt ++;
            }

            max_window = std::max(window, max_window);
        }
        return result + max_window;
    }
};