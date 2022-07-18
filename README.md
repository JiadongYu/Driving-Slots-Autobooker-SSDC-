# Driving-Slots-Autobooker-SSDC
Utilised Python, Selenium, Twilio and Windows task scheduler to automate the booking of practical lesson slots at Singapore Safety And Driving Centre (SSDC)

# Introduction
It is often difficult to obtain driving lesson slots as they are quickly snatched up once they are released. In addition, it is tedious and time-consuming to camp for these slots. This script aims to automate the process of booking driving slots once they become available. In addition, users are promptly notified via text once slots have been reserved for them so they can make payment quickly to secure their slots. Zero coding knowledge is required for new users to configure the script to their own needs. 

# Note
It is recommended to use the latest version of Google Chrome to allow for a smoother user experience and to minimise errors in the running of the script. See the Troubleshooting section for common errors and how to resolve them.

# Step 1: Downloading & Configuring Selenium
Selenium is a piece of software that supports browser automation. We will use it to automate the process of navigating through the SSDC website to find our slots. Selenium (For Google Chrome) can be downloaded at https://sites.google.com/chromium.org/driver/ . You should download the version of Selenium that corresponds to the version of your Chrome browser to prevent incompatabilities and errors later on. Take note of the location of the downloaded Selenium driver as we will use it later on.

# Step 2: Set up a FREE twilio account
Twilio is a piece of software that helps to send automated mobile texts. Please make a free account by following the instructions in this short 5 minute video: https://www.youtube.com/watch?v=ILMuc1KASbo . Please note down the following information as they will be of use in the next step: 1. Account SID 2. Auth Token 3. Your twilio trial number (The phone number that twilio will message you from). 

# Step 3: Download and personalise main.py
main.py is the aforementioned Python-Selenium script. You will be making some minor edits to this script such as by keying in your SSDC login details and your phone number. Open up main.py and enter your SSDC login details, Account SID and Auth Token in lines 11 to 17. Next on line 27, copy your own file path to the Selenium driver that you downloaded earlier in step 1. Finally, navigate to lines 127 - 128 and add your twilio trial number as well as your personal phone number. 

# Step 4: Download Python 
Install Python as per the instructions in this video: https://www.youtube.com/watch?v=Kn1HF3oD19c . Take note of the location in which you installed Python. 

# Step 5: Configure windows task scheduler
Follow the instructions in this video to configure the script to run at intervals of your choosing: https://www.youtube.com/watch?v=n2Cr_YRQk7o . Voila!

# Troubleshooting
Error: Unable to determine loading status /n
Fix: Ensure that you are running the latest versions of selenium webdriver and Google Chrome

Error: Recaptcha failed
Fix: Pause the running of the script in windows task scheduler for 24 hours as the SSDC site suspects that you are a bot and will block further login attempts for around 24 hours.

