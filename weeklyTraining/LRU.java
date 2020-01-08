package weeklyTraining;

import java.util.HashMap;
import java.util.Scanner;

class QNode{
	int key,value;
	QNode prev,next;
	
	public QNode(int key, int value) {
		this.key=key;
		this.value=value;
	}
		}
public class LRU {
	
	int capacity;
	HashMap<Integer, QNode> map=new HashMap<Integer, QNode>();
	QNode head=null;
	QNode end=null;
	public LRU(int capacity) {
		this.capacity=capacity;
	}
	
	public int fetch(int key) {
		if(map.containsKey(key)) {
			QNode n=map.get(key);
			delete(n);
			updateHead(n);
			return n.value;
		}
		return -1;
	}
	
	public void updateHead(QNode n) {
		n.next=head;
		n.prev=null;
		if(head!=null)
			head.prev=n;
		head=n;
		if(end==null)
			end=head;
	}
	
	public void update(int key,int value) {
		if(map.containsKey(key)) {
			QNode oldnode = map.get(key);
			oldnode.value=value;
			delete(oldnode);
			updateHead(oldnode);
		}else {
			QNode newnode = new QNode(key,value);
			if(map.size()>=capacity) {
				map.remove(end.key);
				delete(end);
				updateHead(newnode);
			}else {
				updateHead(newnode);
			}
			map.put(key, newnode);
		}
	}

	public void delete(QNode node) {
		if(node.prev!=null) {
			node.prev.next =node.next;
		}else {
			head=node.next;
		}if(node.next!=null) {
			node.next.prev=node.prev;
		}else {
			end=node.prev;
		}
	}  
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Capacity:\n");
		int capacity=sc.nextInt();
		LRU cache=new LRU(capacity);
		cache.update(1, 12);
		cache.update(2, 32);
		cache.update(11, 43);
		cache.update(2, 51);
		cache.update(3,22);
		cache.update(11, 33);
		System.out.println(cache.fetch(11));
		System.out.println(cache.fetch(2));
	}
	
}
