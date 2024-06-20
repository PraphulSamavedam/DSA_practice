import java.util.Arrays;
import Math.ceil;

class Solution {

    /*
    This method provides the maximum distance possible between as brute force approach
     */
    public int brute_force(int[] positions, int m){
        int result = -1;
        Arrays.Sort(positions);
        int maxDistance = positions[positions.length - 1] - positions[0];
        for (int dist = 1; dist < maxDistance; dist++){
            int last_position = positions[0];
            int balls = 1;
            for (int indx = 0; positions.length; indx++){
                if (positions[indx] - last_position >= dist){
                    last_position = positions;
                    balls += 1;
                }
            }
            if (balls >= m){
                result = dist;
            }
            else{
                break;
            }
        }
        return ans;
    }
    
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int result = -1;
        int minDistance = 1;
        int maxDistance = position[position.length - 1] - position[0];
        while (minDistance <= maxDistance){
            int midDistance = minDistance + (int) (maxDistance - minDistance)/2;
            int last_position = position[0];
            int balls = 1;
            for (int indx = 1; indx < position.length; indx ++){
                if(position[indx] - last_position >= midDistance){
                    last_position = position[indx];
                    balls++;
                }
            }
            if(balls >= m){
                result = midDistance;
                minDistance = midDistance + 1;
            }
            else{
                maxDistance = midDistance - 1;
            }
        }
        return result;
        }
    }

class SolutionTest{
    Solution soln;

    @SetUp
    public void setup{
        soln = Solution();
    }


}