package weeklyTraining;

public class Task4 {
	
	
	public static void main(String[] args) {
	Insertion i = new Insertion();
	TreeNode root = null;
	root = i.insert(root, 8);
	root = i.insert(root, 3);
	root = i.insert(root, 6);
	root = i.insert(root, 10);
	root = i.insert(root, 4);
	root = i.insert(root, 7);
	root = i.insert(root, 1);
	root = i.insert(root, 14);
	root = i.insert(root, 13);
	
	System.out.println("Inorder traversal");
	i.inorder(root);
	
	
	}
	
}  