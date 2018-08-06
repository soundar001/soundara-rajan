import java.io.*;
import java.util.*;
class A
{
public static void main(String Args[])
{
System.out.println("Enter the number");
 Scanner a = new Scanner(System.in);
 int b=a.nextInt();
if(b>0)
{
System.out.println("The given number is positive");
}
else if(b==0)
{
System.out.println("The number is Zero");
}
else
{
System.out.println("The number is negative");
}
}
}
