public class Solution {
    public int solve(int A) {
        int sum1 = 0;
        for(int i=1;i<=A;i++){
            if(i%2==0){
                sum1=sum1+i;
            }
        }
        return sum1;
    }
}
