package weeklyTraining;

import java.util.Scanner;

public class Task5 {
	public static void main(String[] args) {
		Insertion i = new Insertion();
		TreeNode root = null;
		Scanner sc = new Scanner(System.in);
		for(int j=0; j<5;j++) {
		System.out.println("Value to be inserted:\n");
		int val = sc.nextInt();
		root = i.insert(root, val);
		}
		System.out.print("Inorder traversal \t");
		i.inorder(root);
	}
}
