# Cloud-Mark-1

# PROJECT IDEA :CLOUD OPTIGUARD [Intelligent Cost Optimization and Performance Monitoring System for Cloud Workloads]

#Problem Statement
Many companies using cloud services struggle with optimizing their cloud costs and monitoring performance efficiently. They often face challenges such as:

#Setting Up AWS for CloudOptiGuard (Step-by-Step for Beginners)
🔹 Step 1: Create an AWS Account
📌 1.1 Go to AWS Website
Open Google Chrome (or any browser).
Type "AWS free tier" in Google and click the first link (or go directly to AWS Free Tier).
📌 1.2 Start Creating Your AWS Account
Click the “Create a Free Account” button.
It will ask you for an email and password.
Email: Use a Gmail, Outlook, or any active email.
Password: Create a strong password (use letters, numbers, and symbols).
Click “Continue”.
📌 1.3 Fill in Personal Information
Select “Personal” account type.
Enter your Full Name and Mobile Number.
Enter your Address, City, Pin Code, and Country.
Click “Continue”.
📌 1.4 Add Payment Method (Card Details Required)
AWS requires a card to verify your identity, but don’t worry, you won’t be charged if you stay in the free tier.

Enter your debit or credit card details:
Card Number: 16-digit number on the front of your card.
Expiry Date: MM/YY format (e.g., 06/27 for June 2027).
CVV: 3-digit security code (back of the card).
Click “Verify and Continue”.
📝 Important Notes:

Works with international debit/credit cards (Visa/MasterCard/RuPay).
₹2 or $1 may be deducted temporarily (it will be refunded).
📌 1.5 Identity Verification (OTP or Call Verification)
Enter your mobile number for OTP verification.
AWS will send an OTP (6-digit code) to your phone.
Enter the OTP and click “Verify”.
📌 1.6 Select a Support Plan
AWS will ask you to select a Support Plan.
Choose the Free Basic Plan (it’s free).
Click “Continue”.
✅ Congratulations! Your AWS account is now created! 🎉

#Step 2: Sign In to AWS Console
Go to AWS Console.
Click “Sign in”.
Select "Root user" and enter your email & password.
Click "Sign In".
✅ You are now inside the AWS Management Console. 🎉

#Step 3:  Step-by-Step Guide to Creating an AWS Budget Alert
Step 3.1: Open the AWS Billing Dashboard
Go to the AWS Console → Click here
In the top search bar, type → Billing Dashboard
Click on Billing and Cost Management
Step 3.2: Navigate to AWS Budgets
In the left-hand sidebar, find and click Budgets (under Billing and Cost Management)
On the Budgets page, click the blue "Create a Budget" button
Step 3.3: Choose Budget Type
Budget Type: Select Cost Budget (first option)
Click Next
Step 3.4: Define Your Budget Details
Budget Name: Enter → Cloud Budget Alert
Period: Select Monthly
Budget Amount: Set a limit, e.g.,
$0.01 (USD) if you're using USD
Click Next
Step 3.5: Set Up Budget Notifications
Threshold Type: Choose Actual Cost
Threshold Percentage: Enter 100% (so you get an alert when the cost reaches ₹100 or $1)
Notification Recipient: Enter your email ID
Click Next
Step 3.6: Review & Create Budget
Review all details
Click Create Budget
✅ Done! AWS will now send you an email alert if your spending exceeds $0.01

#Step 4: Open EC2 Dashboard
In the AWS Management Console, search for EC2 in the top search bar.
Click on EC2 to open the dashboard.
Start Creating an Instance
Click on "Launch instance" (big orange button).
You'll see a screen titled "Choose an Amazon Machine Image (AMI)".
Choose a Name for Your Instance
At the top, you'll see a text box for "Name and tags".
Enter a name for your instance. You can name it CloudOptiGuard-Test or anything you like.
Choose an AMI (Amazon Machine Image)
Scroll down to the “Application and OS Images (Amazon Machine Image)” section.
Select “Amazon Linux 2023” (it should be in the "Quick Start" list).
This is a free-tier eligible Linux-based OS, perfect for testing.
Keep the x86_64 architecture selected.
Choose an Instance Type
Scroll down to the “Instance Type” section.
Select t2.micro (it should be the default).
✅ It’s free-tier eligible and has 1 vCPU and 1 GB RAM, which is enough for testing.
🔹 Do NOT change anything else here.
Configure Key Pair for SSH Access
Now, we need to set up a key pair so we can securely connect to the instance later.

Scroll down to "Key pair (login)" section.
Click "Create new key pair" (if you don’t have one already).
Set these details:
Key pair name → CloudOptiGuard-Key
Key pair type → RSA (default)
Private key format → .pem (important for SSH access)
Click "Create key pair" → It will download a .pem file.
Keep this file safe (you will need it to SSH into the instance).
Configure Network Settings
Now, we need to set up network access so we can connect to the instance.

Scroll down to "Network settings" section.
Make sure "Allow SSH traffic from" is enabled:
Choose "Anywhere (0.0.0.0/0)" (This allows SSH access from any IP).
⚠️ Security Note: If this is a test instance, it's fine. But for production, restrict access to your own IP.
Click "Edit" under "Security group" and check if there is a rule for:
SSH (Port 22) → Allowed from Anywhere (0.0.0.0/0)
HTTP (Port 80) → (If we need a web server later)
HTTPS (Port 443) → (For secure web traffic)
LAUNCH INSTANCE


