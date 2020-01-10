package weeklyTraining;

public class OperationList {
	int length;
	Node head= null;
	Node tail=null;
	public void addNode(int data) {
		Node node1 = new Node(data);
		if(head==null) {
			head = node1;
			tail = node1;
		}
		else {
			tail.next = node1;
			tail = node1;
		}
		length++;
	}
	
	public void update(int old_val, int new_val) {
		Node current = head;
		while(current!=null && current.data!=old_val) {
			current=current.next;
		}
		if(current!=null) {
			current.data=new_val;
		}
		else {
			System.out.println("The value not found in list");
		}
	}
	
	public void delete(int key) {
		Node temp, current;
		if(head==null) {
			System.out.println("Empty linked list");
		}
		else {
			if(head!=tail) {
				temp=head;
				current=null;
				for(int i=0; i<key-1; i++) {
					current=temp;
					temp=temp.next;
				}
				if(temp!=null) {
					System.out.println("current is null");
					current.next=temp.next;
					temp=null;
				}
				else {
					head=tail=temp.next;
					temp=null;
				}
				
			}
			else {
				head=tail=null;
			}
		}
		
		length--;
	}
	
	public void display() {  
        //Node current will point to head  
        Node current = head;  
        if(head == null) {  
            System.out.println("List is empty");  
            return;  
        }  
  
        while(current != null) {  
            //Prints each node by incrementing pointer  
            System.out.print(current.data + " ");  
            current = current.next;  
        }  
        System.out.println();  
    }  
}
