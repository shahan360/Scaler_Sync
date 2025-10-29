Problem Name: Q2. Product of elements

## Problem Description

Write a program that returns the product of all elements present in the array.

Note: The list with elements is already passed as an argument to the function. User don't need to take any input. Just perform the task on the passed arguments and return the required result.

## Problem Constraints

1 <= |A| <= 100
1 <= A <= 100
Note: It is guaranteed that the resultant product will be <= 1015

## Input Format

. Just perform the task on the passed arguments and return the required result.

Constraints:

1 <= |A| <= 100
1 <= A <= 100
Note: It is guaranteed that the resultant product will be <= 1015

Input Format:

An integer array **A** as the function argument.

## Output Format

Product of elements in integer format

Sample Input:

A = [7, 9, 2, 51]

Sample Output:

6426

Sample explanation:

The product of all the elements is 7 * 9 * 2 * 51 = 6426 is returned.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
// Complete the function template here
// Scanner scn = new Scanner(System.in);
// int N = scn.nextInt();
// int A[] = new int[N];
// for(int i=0;i<N;i++){
//     A[i]=scn.nextInt();
// }
long pro=1;
for(int i=0;i<arr.length;i++){
pro = pro*arr[i];

## Example Input

A = [7, 9, 2, 51]

Sample Output:

6426

Sample explanation:

The product of all the elements is 7 * 9 * 2 * 51 = 6426 is returned.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
// Complete the function template here
// Scanner scn = new Scanner(System.in);
// int N = scn.nextInt();
// int A[] = new int[N];
// for(int i=0;i<N;i++){
//     A[i]=scn.nextInt();
// }
long pro=1;
for(int i=0;i<arr.length;i++){
pro = pro*arr[i];

## Example Output

6426

Sample explanation:

The product of all the elements is 7 * 9 * 2 * 51 = 6426 is returned.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
// Complete the function template here
// Scanner scn = new Scanner(System.in);
// int N = scn.nextInt();
// int A[] = new int[N];
// for(int i=0;i<N;i++){
//     A[i]=scn.nextInt();
// }
long pro=1;
for(int i=0;i<arr.length;i++){
pro = pro*arr[i];

## Example Explanation

The product of all the elements is 7 * 9 * 2 * 51 = 6426 is returned.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
// Complete the function template here
// Scanner scn = new Scanner(System.in);
// int N = scn.nextInt();
// int A[] = new int[N];
// for(int i=0;i<N;i++){
//     A[i]=scn.nextInt();
// }
long pro=1;
for(int i=0;i<arr.length;i++){
pro = pro*arr[i];

## Solution

See `Solution.java` for the implementation.