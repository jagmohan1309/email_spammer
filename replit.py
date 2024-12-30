import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail account credentials
sender_email = "ramshyam11546@gmail.com"  # Your Gmail address
password = "bgwp mbfi mnpq ison"  # Your Gmail password or app-specific password

# Create lists of different subjects and bodies
subjects = [
    "Quick Update for You",
    "Important Information Inside",
    "Check This Out",
    "News You Don't Want to Miss",
    "Special Message for You"
]

body_messages = [
    "I hope this email finds you well. Just wanted to share some important updates with you.",
    "Thank you for your time. Here's some information you might find interesting.",
    "I wanted to reach out and share something exciting with you.",
    "Greetings! I trust you're having a great day. Here's what's new.",
    "Hello there! I have some interesting news to share with you."
]

try:
    # Ask the user for the recipient's email addresses
    recipient_input = input("Enter the recipient email(s), separated by commas: ").strip()
    recipient_emails = [email.strip() for email in recipient_input.split(",")]

    if not recipient_emails:
        raise ValueError("You must enter at least one valid email address.")

    # Start the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Establish a secure connection
        server.login(sender_email, password)  # Log in to the Gmail account

        email_count = 0  # Track the number of emails sent

        while True:
            for recipient in recipient_emails:
                # Get random subject and body
                current_subject = subjects[email_count % len(subjects)]
                current_body = body_messages[email_count % len(body_messages)]

                # Create email
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient
                msg['Subject'] = current_subject
                msg.attach(MIMEText(current_body, 'plain'))

                # Send the email
                server.sendmail(sender_email, recipient, msg.as_string())
                email_count += 1
                print(f"Email sent to {recipient} (Total sent: {email_count})")

            # Ask the user if they want to continue
            continue_sending = input("Do you want to continue sending emails? (yes/no): ").strip().lower()
            if continue_sending != 'yes':
                print(f"Email sending stopped. Total emails sent: {email_count}")
                break

except ValueError as ve:
    print(f"Input error: {ve}")

except Exception as e:
    print(f"An error occurred: {e}")
