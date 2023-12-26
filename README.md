
---

# Tinder Bot

This Python script uses Selenium to automate interactions with the Tinder website, allowing you to perform actions like logging in, swiping, and sending messages to matches.

## Setup Instructions

### 1. Install Dependencies

- **Python 3.x:** Make sure you have Python 3.x installed on your system.
- **Selenium:** Install the Selenium package using pip:

    ```
    pip install selenium
    ```

### 2. Download Chrome WebDriver

- Download the Chrome WebDriver compatible with your Chrome browser version from the [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/) page.
- Extract the downloaded zip file and place the `chromedriver` executable in a location accessible from your system's PATH environment variable.

### 3. Set Up Login Details

- Create a file named `login_details.py` in the same directory as your script.
- Define variables `phone` and `password` in `login_details.py` with your Tinder login credentials:

    ```python
    phone = "your_phone_number"
    password = "your_password"
    ```

## Running the Script

- Run the script using Python:

    ```
    python tinder_bot.py
    ```

# Overview

The Tinderbot class is designed to automate interactions with the Tinder web application using Selenium. It performs actions such as accepting cookies, logging in with Facebook, swiping right on profiles, handling pop-ups, and sending messages to matches.

## Usage
To use the Tinderbot class:

- Ensure you have the required dependencies installed, including Selenium and a compatible WebDriver (e.g., ChromeDriver for Chrome).
- Provide valid login details in a file named login_details.py, containing phone and password variables.
- Instantiate the Tinderbot class and call its open_driver() method to start the automation.

## Flow of the Code
- Initialization: The Tinderbot class initializes a Chrome WebDriver and a WebDriverWait instance with a timeout of 10 seconds.

- Open Driver: The open_driver() method navigates to the Tinder website, accepts cookies, and logs in with Facebook using provided login details.

- Autoswipe: The autoswipe() method continuously attempts to swipe right on profiles. If an exception occurs during the right swipe, it attempts to handle it by clicking on the "add home" element. If that also fails, it calls the close_match() method.

- Close Match: The close_match() method handles the closing of the match popup.

- Get Matches: The get_matches() method retrieves a list of match profiles and filters out the user's own profile link.

- Send Messages to Matches: The send_messages_to_matches() method sends a predefined message to each match retrieved from the previous step using the send_message() method.

- Send Message: The send_message() method navigates to a match's profile and sends a predefined message.

- Main Function: The main() function instantiates the Tinderbot class, opens the driver, and sends messages to matches.

- Execution: The if __name__ == "__main__" block executes the main() function when the script is run directly.

## Notes
Ensure that the XPath expressions used to locate elements on the page are up-to-date and reliable.
Add appropriate error handling and logging to handle exceptions and unexpected behavior.
Test the script thoroughly in a controlled environment before using it for actual interactions on Tinder.
### Also please take care or check in terms of matches as I am not attractive so I did not get any matches, let me know if it works or not


---
