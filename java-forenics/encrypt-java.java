import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class Encryption {
	public static void main(String[] args)
	
		throws FileNotFoundException, IOException
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Note : Encryption Key act as Password to Decrypt the same Image,otherwise it will corrupt the Image." + 
		"\n" + "JAVA TROJAN ENCRYPTION");
		
		//*************************************************//
			
		System.out.println("Place image file to encrypt : ");
		String path = s.nextLine();
		
		//*************************************************//
	
		System.out.print("Enter key for Encryption : ");
		int key = s.nextInt();
	
		FileInputStream fis = new FileInputStream(path);					
		byte data[] = new byte[fis.available()];
						
		fis.read(data);
		int i = 0;
	
		for (byte b : data) {
			data[i] = (byte)(b ^ key);
			i++;
		}
					
		FileOutputStream fos = new FileOutputStream(path);
							
		fos.write(data);
							
		fos.close();
		fis.close();
		System.out.println("Encryption happen now...");
	}
}

