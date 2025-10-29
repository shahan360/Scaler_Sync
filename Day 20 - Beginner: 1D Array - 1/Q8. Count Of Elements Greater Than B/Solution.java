public class Solution {
    public int solve(int[] A, int B) {
        int N = A.length;
        int count=0;
        for(int i=0;i<N;i++){
            if(A[i]>B){
                count++;
            }
        }
        return count;
    }
}
