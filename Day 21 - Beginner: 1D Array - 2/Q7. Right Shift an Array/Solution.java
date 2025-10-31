import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [] arr = new int [n];
       
        for(int i = 0;i < n;i++){
            arr[i] = sc.nextInt();
        }

        int temp = arr[n - 1];

        for(int i = n - 1; i > 0; i--){
            arr[i] = arr[ i - 1];
        }
        arr[0] = temp;

        for(int i = 0;i < n; i++){
            System.out.print(arr[i] + " ");
        }
        
    }
}