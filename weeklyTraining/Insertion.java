package weeklyTraining;

import java.util.*;

public class Insertion {
	static TreeNode root;
	static TreeNode temp = root;
	//inorder traversal with recursion
	/*static void inorder(TreeNode temp)
	{
		if(temp==null)
		{
			return;
		}
		inorder(temp.left);
		System.out.println(temp.data+" ");
		inorder(temp.right);		
	}*/
	
	//inorder traversal without recursion 
	static TreeNode pushArr(TreeNode node, ArrayList<Integer> value) {
		
		TreeNode prev=null;

		while(node.left!=null) {
			prev=node;
			node=node.left;
			value.add(node.data);
		}
		return prev;

	}
	
	static void inorder(TreeNode root) {

		TreeNode current = root;
		Stack<TreeNode> value=new Stack<TreeNode>();
		while (current != null || !value.isEmpty()) {			
			while (current != null) {
				value.push(current);
				current = current.left;
			}
			if (current == null && !value.isEmpty()) {
				TreeNode popped=value.pop();
				System.out.println(popped.data + " popped item");
				current = popped.right;
			}
		}
		
		
	}
	
	public TreeNode createNewNode(int k)
	{
		TreeNode i = new TreeNode();
		i.data=k;
		i.left=null;
		i.right=null;
		return i;
	}
	public TreeNode insert(TreeNode node,int val)
	{
		if(node==null) 
		{
			return createNewNode(val);
		}
		if(val<node.data)
		{
			node.left = insert(node.left,val);
		}
		else if(val>node.data)
		{
			node.right = insert(node.right,val);
		}
		return node;
	}

}
