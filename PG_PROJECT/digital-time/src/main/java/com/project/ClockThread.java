package com.project;

import java.text.SimpleDateFormat;
import java.util.Date;

public class ClockThread extends Thread
{
	
	DigitalTime dc;
	
	
	public ClockThread(DigitalTime digitalClock)
	{
		
		this.dc = digitalClock;
		start();
	}
	
	public void run()
	{
		while(true)
		{
			Date date = new Date();
			SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
			String formatDate = sdf.format(date);
			
			
			String[] dateArr = formatDate.split(":");
			
			dc.textField.setText(dateArr[0]);
			dc.textField_1.setText(dateArr[1]);
			dc.textField_2.setText(dateArr[2]);

		}
	}
	
}
