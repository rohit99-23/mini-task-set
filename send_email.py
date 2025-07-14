import smtplib  
from email.mime.text import MIMEText  # Text message banane ke liye
from email.mime.multipart import MIMEMultipart  # Multiple part email (subject, body, etc.) banane ke liye

# 1. Email ka basic setup
sender_email = input("Enter Sender Email:")  # Jis email se bhejna hai
receiver_email = input("receiver_email@example.com")  # Jis email pe bhejna hai
subject = input("Test Email from Python")
body = input("Hello, yeh ek test email hai jo Python se bheji gayi hai!")

# 2. Agar aapke Gmail me 2FA (Two Factor Authentication) ON hai, toh aapko "App Password" generate karna padega
password = input("your_app_password")  # Gmail ka App Password yahan daalein (na ki apna regular Gmail password)

# 3. Email message bana rahe hain
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# 4. Message ke andar actual body add kar rahe hain
message.attach(MIMEText(body, "plain"))

# 5. Gmail SMTP server ke through email bhejna
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure connection banate hain (TLS)
        server.login(sender_email, password)  # Apne Gmail se login karte hain
        server.sendmail(sender_email, receiver_email, message.as_string())  # Email bhej dete hain
        print("✅ Email successfully send")
except Exception as e:
    print("❌ Email don't send", e)
