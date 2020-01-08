package weeklyTraining2;

import java.util.*;

public class String2 {
	static boolean isEqlFreq(int[] count) {
		boolean flag=false;
		int i,j;
		for(i=0;i<count.length;i++) {
			for(j=i+1;j<count.length;j++) {
				while(count[i]!=count[j]) {
					flag=true;
				}
				break;
				//flag=false;
				
			}
		}
			return flag;
	}
public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	String str4 =sc.nextLine();
	int count[]=new int[str4.length()];
	char[] str3 = str4.toCharArray();
	int i,j;
	for(i=0;i<str4.length();i++) {
		count[i]=1;
		for(j=i+1;j<str4.length();j++) {
			if(str3[i]==str3[j]) {
				count[i]++;
			
			str3[j]= '0';
			}
		}
	}
	System.out.println("Are all the characters having same frequencies "+ isEqlFreq(count));
}

}
