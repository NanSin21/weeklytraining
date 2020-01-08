package weeklyTraining;

public class Insertion {
	static TreeNode root;
	static TreeNode temp = root;
	static void inorder(TreeNode temp)
	{
		if(temp==null)
		{
			return;
		}
		inorder(temp.left);
		System.out.println(temp.data+" ");
		inorder(temp.right);		
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
