

# Import the necessary libraries
import time
from selenium import webdriver
from selenium.common import ElementNotInteractableException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from twilio.rest import Client

# Configure twilio
account_sid = 'AC719bfd577b35856261884872a9db39f3'
auth_token = '3d41284f58b1e54fa7c5197abe4fee92'

# Set SSDC login details
myUserName = 827544
myPassword = "Superman333!"

# Track whether user has logged in
loggedIn = False

# Track if there are any available slots left (Set as true by default)
slotsAvailable = True

# Create a driver for google chrome
s = Service("C:\Program Files (x86)\chromedriver.exe")

# Log in and handle recaptcha failures
while not loggedIn:
    # First step when using selenium is to select which browser we are using
    driver = webdriver.Chrome(service=s)  # Create an instance of the webdriver object which has been configured to the
    # Maximize window
    driver.maximize_window()
    # Navigate to the SSDC website
    driver.get("https://www.ssdcl.com.sg/User/Login")

    # In selenium, we find the element first before we tell the element what to do
    username = driver.find_element(By.ID, "UserName")
    password = driver.find_element(By.ID, "Password")
    # Clear any pre-populated fields
    username.clear()
    password.clear()
    username.send_keys(myUserName)
    password.send_keys(myPassword)
    # Attempt to log in by selecting the Login button
    log_in = driver.find_element(By.CSS_SELECTOR, ".float-right")
    log_in.click()
    # Handle recaptcha failure
    try:
        close = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//button[text()="Close"]'))
        )
        close.click()
        print("recaptcha failed")
        driver.quit()
        continue
    except ElementNotInteractableException:
        print("Passed Recaptcha Validation")
        loggedIn = True


# Create a logout function
def logout():
    logoutbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnLogout')))
    logoutbutton.click()
    print("Logged out")
    print("Program over")
    driver.quit()


# Navigate to bookings
try:
    bookings = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[text()="Booking and Cancellation"]'))
    )
    bookings.click()

    # Click on make new booking
    newBooking = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "btnNewBooking")))
    newBooking.click()

    # Click on disclaimer
    disclaimer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "chkProceed")))
    disclaimer.click()

    # Proceed to next page
    proceed = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "lnkProceed")))
    proceed.click()

except TimeoutException:
    print("One of the elements could not be loaded")
    logout()

try:
    # Check for availability
    while slotsAvailable:
        # Check for any available slots
        availability = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_checkforava")))
        availability.click()
        driver.execute_script("window.scrollTo(0,125"
                              "0)")
        # find multiple elements
        tableData = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td a")))
        # If no available slots, quit
        if len(tableData) == 0:
            slotsAvailable = False
            break
        else:
            # If slot is available, book a slot by clicking on it
            tableData[0].click()
            # Acknowledge the booking and close the pop-up
            bookingAcknowledgement = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-content .modal-footer button")))
            time.sleep(2)
            bookingAcknowledgement.click()
            # Text the user
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body="🚗 A practical lesson slot has been reserved for you!"
                     " Please make payment in the next 10 minutes!",
                from_='+15672323139',
                to='+6591593869'
            )
            print("Booking has been acknowledged")

except TimeoutException:
    print("No slots were found!")


finally:
    driver.quit()
