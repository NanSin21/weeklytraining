package weeklyTraining2;

import java.util.Scanner;

public class MatrixTask {
	public static int len;
	public static int i,j;

	static boolean isSubset(int[][] small, int[][] main, int s, int e) {
		int k,l;
		int arr[][]=new int[50][50];
		for(i=s, k=0; i<s+small.length; i++,k++) {
			for(j=e, l=0; j<e+small.length;j++,l++) {
				arr[k][l]=main[i][j];
				}
			
		}
		if(isMatch(small, arr)) {
			
			return true;
			
		}
		else {
			return false;
		}
	
	}
	static boolean isMatch(int A[][], int B[][]) 
   { 
	   
		int i, j; 
        for (i = 0; i < A.length; i++) 
            for (j = 0; j < A.length; j++) 
                if (A[i][j] != B[i][j]) 
                    return false; 
            return true; 
   } 
	
	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);
		
		//int len=sc.nextInt();//taking input for size of row and column
		//System.out.println("column size");
		//int lenm=sc.nextInt();//taking input for size of column
		int small[][] = {{2,3},{5,2}};//another smaller 2d matrix
		int main[][] = {{1,2,3},{2,3,6},{5,2,6}};//main matrix
		System.out.println("small"+small.length);
		System.out.println("main"+main.length);
		for(int s=0;s<main.length-1;s++) {
			for(int e=0;e<main.length-1;e++) {
				System.out.println(isSubset(small, main, s,e));
			}
		}
			
		
	}

}
