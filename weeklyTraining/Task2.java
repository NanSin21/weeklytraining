package weeklyTraining;

import java.util.*;

public class Task2 {
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ArrayList<Integer> values= new ArrayList();
		int sum = 1;
		long start = System.currentTimeMillis();
		//inserting 10000 values in collection
		for(int i=0; i<10000; i++) {
			sum = sum+1;
			values.add(sum);
		}
		System.out.println(values);
		long end = System.currentTimeMillis();
		System.out.println("Inserting task takes " + (end - start) + "ms");
	
		Scanner sc = new Scanner(System.in);
	
	//updating a position with user value
	System.out.println("Index for updation");
	int user= sc.nextInt();
	System.out.println("Value to be updated");
	int user2= sc.nextInt();
	values.set(user, user2);
	long end1 = System.currentTimeMillis();
	System.out.println("Inserting task takes " + (end1 - end) + "ms");
	
	//deleting a position with user value
	System.out.println("Index tobe deleted");
	int user3= sc.nextInt();
	values.remove(user3);
	long end2 = System.currentTimeMillis();
	System.out.println("Inserting task takes " + (end2 - end1) + "ms");
	
	System.out.println(values);
	long end3 = System.currentTimeMillis();
	System.out.println("Inserting task takes " + (end3 - end2) + "ms");
 }

}
