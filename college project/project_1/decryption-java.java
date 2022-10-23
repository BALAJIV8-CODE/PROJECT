import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;
//password : 152000
public class Decryption 
{

	public static void main(String[] args)
	
		throws FileNotFoundException, IOException
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Note : Encryption Key act as Password to Decrypt the same Image, otherwise it will corrupt the Image." +
							"\n" + "JAVA TROJAN DECRYPTER ");
		
		//*************************************************//
			
		System.out.println("Place image file to deccryption : ");
		String path = s.nextLine();
		
		//*************************************************//
	
		System.out.print("Enter a key for Decryption : ");
		int key = s.nextInt();
		
		FileInputStream fis = new FileInputStream(path);
		
		byte data[] = new byte[fis.available()];
		
		fis.read(data);
		int i = 0;
		
		for (byte b : data) 
		{
			data[i] = (byte)(b ^ key);
			i++;
		}
		
		FileOutputStream fos = new FileOutputStream(path);
		fos.write(data);
		fos.close();
		fis.close();
		System.out.println("Decryption happen now...");
	}
}