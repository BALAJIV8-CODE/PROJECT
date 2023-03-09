package com.project;

import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.FontFormatException;
import java.io.IOException;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.JLabel;
import java.awt.Button;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class DigitalClock {

	private JFrame frame;
	JTextField textField;
	JTextField textField_1;
	JTextField textField_2;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					DigitalClock window = new DigitalClock();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public DigitalClock() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 546, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setUndecorated(true);
		frame.setLocationRelativeTo(null);
		frame.getContentPane().setLayout(null);
		
		
		
		Font f = null;
		
		try {
			 f = Font.createFont(Font.TRUETYPE_FONT, DigitalClock.class.getResourceAsStream("/Open24DisplaySt.ttf"));
		} catch (FontFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
		
		
		JPanel panel = new JPanel();
		panel.setForeground(Color.BLACK);
		panel.setBackground(Color.BLACK);
		panel.setBounds(0, 0, 546, 300);
		frame.getContentPane().add(panel);
		panel.setLayout(null);
		
		textField = new JTextField("22");
		textField.setBounds(28, 84, 119, 112);
		textField.setForeground(new Color(255, 255, 255));
		textField.setBackground(Color.BLACK);
		textField.setFont(f.deriveFont(Font.BOLD , 100f));
		textField.setHorizontalAlignment(SwingConstants.CENTER);
		textField.setBorder(null);
		textField.setEditable(false);
		panel.add(textField);
		textField.setColumns(10);
		
		textField_1 = new JTextField("00");
		textField_1.setBounds(213, 84, 119, 112);
		textField_1.setForeground(new Color(255, 255, 255));
		textField_1.setBackground(Color.BLACK);
		textField_1.setFont(f.deriveFont(Font.BOLD , 100f));
		textField_1.setHorizontalAlignment(SwingConstants.CENTER);
		textField_1.setBorder(null);
		textField_1.setEditable(false);
		panel.add(textField_1);
		textField_1.setColumns(10);
		
		textField_2 = new JTextField("08");
		textField_2.setBounds(396, 84, 119, 112);
		textField_2.setForeground(new Color(255, 255, 255));
		textField_2.setBackground(Color.BLACK);
		textField_2.setFont(f.deriveFont(Font.BOLD , 100f));
		textField_2.setHorizontalAlignment(SwingConstants.CENTER);
		textField_2.setBorder(null);
		textField_2.setEditable(false);
		panel.add(textField_2);
		textField_2.setColumns(10);
		
		JLabel lblNewLabel = new JLabel(":");
		lblNewLabel.setBounds(157, 84, 45, 112);
		lblNewLabel.setForeground(Color.WHITE);
		lblNewLabel.setFont(f.deriveFont(Font.BOLD , 100f));
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		panel.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel(":");
		lblNewLabel_1.setBounds(330, 85, 45, 112);
		lblNewLabel_1.setForeground(Color.WHITE);
		lblNewLabel_1.setFont(f.deriveFont(Font.BOLD , 100f));
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		panel.add(lblNewLabel_1);
		
		Button button = new Button("EXIT");
		button.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		button.setBounds(232, 241, 70, 22);
		panel.add(button);
		
		
	
		new ClockThread(this);
	
	}
}
