package weeklyTraining;

import java.util.LinkedList;
import java.util.Scanner;

public class Task3 {
	
	public static void main(String[] args) {
		OperationList op = new OperationList();
		op.addNode(22);
		op.addNode(13);
		op.addNode(12);
		op.addNode(5);
		op.display();
		op.update(12, 10);
		op.display();
		op.delete(6);
		op.display();
	}
	}
