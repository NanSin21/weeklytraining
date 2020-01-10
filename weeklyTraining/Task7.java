package weeklyTraining;

import java.util.Scanner;

public class Task7 {
	TreeNode root;
	//to check if sum of path equals to given sum
	boolean hasPathSum(TreeNode node, int sum){
		if(node==null) {
			return (sum==0);
		}
		else {
			boolean result = false;
			int subsum= sum-node.data;
			if (subsum == 0 && node.left == null && node.right == null) 
                return true; 
            if (node.left != null) 
                result = result || hasPathSum(node.left, subsum); 
            if (node.right != null) 
                result = result || hasPathSum(node.right, subsum); 
            return result; 
		}
	}
	
	//to print the hierarchies
	void printArr(int arrays[], int size) {
		for(int i=0; i<size; i++) {
			System.out.print(arrays[i]+ " ");
		}
		System.out.println("");
	}
	
	void printPathsRecur(TreeNode node, int path[], int pathlen) {
		if(node==null)
			return;
		path[pathlen]=node.data;
		pathlen++;
		if(node.left==null && node.right==null) {
			printArr(path, pathlen);
		}
		else {
			printPathsRecur(node.left,path,pathlen);
			printPathsRecur(node.right,path,pathlen);
		}
	}
	
	void printPath(TreeNode node) {
		int path[] = new int[200];
		printPathsRecur(node, path, 0);
	}
	
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int sum=sc.nextInt();
		//int sum=21;
		Task7 tree = new Task7(); 
        tree.root = new TreeNode(10); 
        tree.root.left = new TreeNode(8); 
        tree.root.right = new TreeNode(2); 
        tree.root.left.left = new TreeNode(3); 
        tree.root.left.right = new TreeNode(5); 
        tree.root.right.left = new TreeNode(2); 
   
        if (tree.hasPathSum(tree.root, sum)) 
            System.out.println("There is a root to leaf path with sum " + sum); 
        else
            System.out.println("There is no root to leaf path with sum " + sum); 
        
        tree.printPath(tree.root);
    } 
	}

