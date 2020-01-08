package weeklyTraining2;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class StringSecond {
	
	static boolean isPalindrome(String string) {
		String reverse="";
		for(int i=string.length()-1;i>=0;i--) {
			reverse=reverse+string.charAt(i);
			}
		if(string.equals(reverse)) {
			return true;
		}else {
			return false;
		}
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String palstring=sc.nextLine();//original string
		ArrayList<String> str1= new ArrayList();//unique substring array
		ArrayList<String> str2= new ArrayList();//palindrome substring array
		int start, end;
		for(start=0;start<palstring.length(); start++) {
			for(end=palstring.length(); end>start;end--) {
				String new_str=palstring.substring(start, end);
				//str1.add(new_str);
				boolean found=str1.contains(new_str);
				if(!found)
				{
					str1.add(new_str);
				}
			}
		}
		for(String strnew: str1) {
			if(isPalindrome(strnew))
				str2.add(strnew);
		}
		Iterator it = str2.iterator();
		while(it.hasNext()) {
			System.out.println(it.next());
		}
	}
}
