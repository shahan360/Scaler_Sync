public class Solution {
    public int solve(int[] A) {
        for (int i=1;i<A.length;i++){
            if(A[i]<A[i-1]){
                return 0;
            }
        }
        return 1;
    }
}
