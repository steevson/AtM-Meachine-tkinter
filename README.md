# ATM Machine using Tkinter

## Description
This project is a Python-based ATM simulation application that allows users to:
![firstpageATM](https://github.com/user-attachments/assets/532024f6-85d5-4f97-bfdb-84d9a3454f90)

![ATM2](https://github.com/user-attachments/assets/ad2e4deb-a898-49de-856a-1961b88e885e)

- Deposit money into their account.
- Withdraw money from their account.
- Check their account balance.
- Create a new account.
- download receipts
- download ministatment
- Send transaction receipts via email.

The application features a graphical user interface (GUI) built with Tkinter and connects to a MySQL database using pymysql to store and retrieve account information. Transaction details are sent via email using the smtplib library.

## Features
- **Login with PIN**: Users log in by entering their phone number (used as the PIN).
- **Deposit Money**: Users can deposit money into their accounts.
- **Withdraw Money**: Users can withdraw money, with balance checks to ensure sufficient funds.
- **Check Balance**: Users can check the balance of their accounts.
- **Mini Statements**: Users can view a mini-statement after each transaction, which is also saved as a text file.
- **Email Notifications**: After each transaction, users receive an email with a receipt and transaction details.
- **Account Creation**: New users can create accounts by providing their personal details.

## Libraries Used
- **Tkinter**: For creating the GUI.
- **pymysql**: To interact with the MySQL database.
- **smtplib**: For sending emails.
- **ssl**: For secure email sending.
- **PIL (Pillow)**: For handling images in the GUI.

- # This is for the people who using this code for making Tkinter ATM project
- ## 1, first you have to create a table in mysql database ( here i used database name bank. inside bank i created table sbi,were users details  are stored)
- (see the picture as i worked)
-  ![atm_sql](https://github.com/user-attachments/assets/871e0140-3f9e-48ab-a494-07db5eea84a1)
- ## 2, make changes in images i used in this program otherwise it will show errors....
-
