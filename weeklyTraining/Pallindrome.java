package weeklyTraining;

import java.util.Scanner;

public class Pallindrome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("give the string");
		
		
		if(isPallin(sc.nextLine())) {
			System.out.println("Palindrome exists");
		}
		else {
			System.out.println("Palindrome doesnt exist");
		}
	}

	private static boolean isPallin(String user) {
		int i=0,j=user.length()-1;
		while(i<j) {
			if(user.charAt(i)!=user.charAt(j))
				return false;
			i++;
			j--;
		}
		return true;
		
	}

}
