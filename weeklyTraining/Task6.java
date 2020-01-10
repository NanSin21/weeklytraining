package weeklyTraining;

import java.util.Scanner;

public class Task6 {
	   
    public static class Node{  
    int data;  
    Node left;  
    Node right;  

    public Node(int data){  
          
        this.data = data;  
        this.left = null;  
        this.right = null;  
    }  
  }  

    
  public Node root;  

  public Task6(){  
    root = null;  
  }  

    
  public int calculateSum(Node temp){  
    int sum, sumLeft, sumRight;  
    sum = sumRight = sumLeft = 0;  

      
    if(root == null) {  
        System.out.println("Tree is empty");  
        return 0;  
    }  
    else {  
          
        if(temp.left != null)  
            sumLeft = calculateSum(temp.left);  

         
        if(temp.right != null)  
            sumRight = calculateSum(temp.right);  

          
        sum = temp.data + sumLeft + sumRight;  
        return sum;  
    }  
  }  

  public static void main(String[] args) {  

    Task6 bt = new Task6();  
     
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

      
    System.out.println("Sum of all nodes of binary tree: " + bt.calculateSum(bt.root));  
  }  
}
