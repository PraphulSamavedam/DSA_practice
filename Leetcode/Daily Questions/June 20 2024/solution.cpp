class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());

        int result = -1;
        int minD = 1;
        int maxD = position[position.size() - 1];

        while (minD <= maxD){
            int midD = minD + int((maxD - minD)/2);
            int balls = 1;
            int last_posn = position[0];
            for (int posn: position){
                if (posn - last_posn >= midD){
                    last_posn = posn;
                    balls += 1;
                }
            }

            if (balls >= m){
                result = midD;
                minD = midD + 1;
            }
            else{
                maxD = midD - 1;
            }
        }

        return result;
    }
};