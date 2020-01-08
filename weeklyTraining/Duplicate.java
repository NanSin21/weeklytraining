package weeklyTraining;

import java.util.Scanner;

public class Duplicate {
        public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		String string=sc.nextLine();
				
		String words[]=string.split("\\s+");
		String words_new[] =new String[50];
		words_new[0]=words[0];
		int size=1,count=0,j=0,i=0;
		
		for(i=1;i<words.length;i++)
		{
			count=0;
			for(j=0;words_new[j]!=null;j++)
			{
				if(!words[i].equals(words_new[j]))
				{
					count++;
				}
			}
			if(count==size) 
			{
				
				words_new[j]=words[i];
				
				size++;
				
			}
		}
		
		for(i=0;words_new[i]!=null; i++) {
			System.out.print(words_new[i] + " ");
			}
    }
}

