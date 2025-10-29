public static long solve(int[] arr) {
    // Complete the function template here
    // Scanner scn = new Scanner(System.in);
    // int N = scn.nextInt();
    // int A[] = new int[N];
    // for(int i=0;i<N;i++){
    //     A[i]=scn.nextInt();
    // }
    long pro=1;
    for(int i=0;i<arr.length;i++){
        pro = pro*arr[i];
    }
    return pro;

}