package weeklyTraining2;

import java.util.Scanner;

public class MatrixTask {
	public static int len;
	public static int i,j;
	public static boolean isSubset(int n[][], int a[][],int s,int e) {
		 int count = 0;
	        for(int i=s,y=0;i<s+2;i++,y++)
	        {
	            for(int j=e,z=0;j<e+2;j++,z++)
	            {
	                if(n[y][z] != a[i][j])
	                {
	                    count++;
	                }
	            }
	        }
	        if(count >0)
	        {
	            return false;
	        }
	        else
	            return true;
	    
	}
	
	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);
		System.out.println("row size");
		int len=sc.nextInt();//taking input for size of row and column
		//System.out.println("column size");
		//int lenm=sc.nextInt();//taking input for size of column
		int n[][] = {{1,2},{2,3}};//another smaller 2d matrix
		int a[][] = new int[100][100];//main matrix
		for( i=0; i<len; i++) {
			for(j=0; j<len; j++) {
				for(int k=1; k<len; k++) {
					for(int l=1; l<len; l++) {
							a[i][j]= i+j;//values of main matrix be the sum of row and column
				 //n[k][l]=k+l; 
				}
			 }
			}
		}
		for(i=0; i<len; i++) {
			for(j=0;j<len; j++) {
		System.out.print(a[i][j] + " ");
		//printing the values of main array
			}
			System.out.println("");
			
		}
		/*for(i=1; i<len; i++) {
			for(j=1;j<len; j++) {
		System.out.print(n[i][j] + " ");
		//printing the values of main array
			}
			System.out.println("");
		}*/
		System.out.println(isSubset(n, a,0,1));
	}

}
