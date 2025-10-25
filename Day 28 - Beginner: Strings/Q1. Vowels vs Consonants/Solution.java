import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine(); // Consume the newline character after reading t

        for (int i = 0; i < t; i++) {
            int vowels = 0;
            int consonants = 0;
            String s = sc.nextLine();
            for (int j = 0; j < s.length(); j++) {
                char ch = s.charAt(j);
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || 
                    ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
                    vowels++;
                } else if (Character.isLetter(ch)) {
                    consonants++;
                }
            }
            System.out.println(vowels + " " + consonants);
        }
    }
}