public class Solution {
    public int solve(int[] A, int B) {
        int N = A.length;
        for(int i=0;i<N;i++){
            if(A[i]==B){
                return i;
            }
        }
        return -1;
    }
}
