package weeklyTraining;

import java.util.Scanner;

public class SameString {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		String str1 = sc.nextLine();
		if(str.equals(str1)) {
			System.out.println("Same string present");
		}
		else {
			System.out.println("Not same");
		}
	}
}
