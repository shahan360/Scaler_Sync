import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner scn = new Scanner(System.in);
        int N = scn.nextInt();
        int A[] = new int[N];
        for(int i=0;i<N;i++){
            A[i]=scn.nextInt();
        }
        for(int i=0;i<A.length;i++){
            if(A[i]<0){
                System.out.print(A[i]+" ");
            }
        }
        
    }
}