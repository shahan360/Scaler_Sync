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
        int aran[] = new int[N];
        for(int i=0;i<N;i++){
            aran[i]=scn.nextInt();
        }
        int sum = 0;
        for(int i=0;i<aran.length;i++){
            sum = sum + aran[i];
        }
        int avgx = sum/aran.length;
        System.out.print(avgx);

        
    }
}