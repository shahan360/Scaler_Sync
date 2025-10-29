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
        int temp[] = new int[N];
        for(int i=0;i<N;i++){
            temp[i]=scn.nextInt();
        }
        int max = 0;
        int min = 0;
        for(int i=0;i<temp.length;i++){
            if(temp[i]>max){
                max=temp[i];
            }
            if(temp[i]<min){
                min=temp[i];
            }
        }
        System.out.print(max-min);
        
    }
}