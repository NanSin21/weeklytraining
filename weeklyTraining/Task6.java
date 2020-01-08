package weeklyTraining;

import java.util.Scanner;

public class Task6 {
	 //Represent the node of binary tree  
    public static class Node{  
    int data;  
    Node left;  
    Node right;  

    public Node(int data){  
        //Assign data to the new node, set left and right children to null  
        this.data = data;  
        this.left = null;  
        this.right = null;  
    }  
  }  

  //Represent the root of binary tree  
  public Node root;  

  public Task6(){  
    root = null;  
  }  

  //calculateSum() will calculate the sum of all the nodes present in the binary tree  
  public int calculateSum(Node temp){  
    int sum, sumLeft, sumRight;  
    sum = sumRight = sumLeft = 0;  

    //Check whether tree is empty  
    if(root == null) {  
        System.out.println("Tree is empty");  
        return 0;  
    }  
    else {  
        //Calculate the sum of nodes present in left subtree  
        if(temp.left != null)  
            sumLeft = calculateSum(temp.left);  

        //Calculate the sum of nodes present in right subtree  
        if(temp.right != null)  
            sumRight = calculateSum(temp.right);  

        //Calculate the sum of all nodes by adding sumLeft, sumRight and root node's data  
        sum = temp.data + sumLeft + sumRight;  
        return sum;  
    }  
  }  

  public static void main(String[] args) {  

    Task6 bt = new Task6();  
    //Add nodes to the binary tree 
    Scanner sc = new Scanner(System.in);
    System.out.println("root");
    bt.root = new Node(sc.nextInt());  
    System.out.println("2nd node");
    bt.root.left = new Node(sc.nextInt());  
    System.out.println("3rd node");
    bt.root.right = new Node(sc.nextInt());  
    System.out.println("4th node");
    bt.root.left.left = new Node(sc.nextInt());  
    System.out.println("5th node");
    bt.root.right.left = new Node(sc.nextInt());  
    System.out.println("6th node");
    bt.root.right.right = new Node(sc.nextInt());  

    //Display the sum of all the nodes in the given binary tree  
    System.out.println("Sum of all nodes of binary tree: " + bt.calculateSum(bt.root));  
  }  
}
