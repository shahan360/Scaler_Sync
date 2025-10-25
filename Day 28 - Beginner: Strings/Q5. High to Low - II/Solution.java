public class Solution {
    public String solve(String A) {
        String resStr = "";

        for(char ch: A.toCharArray()){ //converts String to char Arr
            resStr += (char)(ch + 32); // ch is char so its ascii is there
        // difference between lower and uppercase in ascii is 32 to we add 32 to ch
        }
        return resStr;
    }
}
