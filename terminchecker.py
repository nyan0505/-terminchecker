from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Returns the shadow DOM of the given element
def get_shadow_root(element, driver):
    return driver.execute_script('return arguments[0].shadowRoot', element)

#Open chrome 
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")  

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://stadt.muenchen.de/buergerservice/terminvereinbarung.html#/services/10339027/locations/10187259')
print("page loaded")
time.sleep(5)
# Get the shadow root of an element
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "zms-appointment")))
shadow_host = driver.find_element(By.TAG_NAME, "zms-appointment")  
time.sleep(5)
shadow_root = get_shadow_root(shadow_host,driver)
print("found shadow root")

#Click the button to go to the Termin selection window
button = WebDriverWait(shadow_root, 10).until(
    lambda x: x.find_element(By.CLASS_NAME, "button-next")
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
time.sleep(5)
button.click()
print("button clicked")

    
time.sleep(2)

#find the text 'Keine freien Termine verfügbar'
text_element = WebDriverWait(shadow_root, 10).until(
    lambda x: x.find_element(By.CLASS_NAME, "m-callout--warning")
)
if text_element:
    print('Keine freien Termine verfügbar')
else:
    print('freie Termine verfügbar')

    #Send email
    #add sender and receiver emails
    #use gmail app password of sender email
    sender_email = "sender@example.com"
    receiver_email = "receiver@example.com"
    password = "password"

    subject = "Terminvereinbarung ist im Ausländeramt München möglich"
    body = """
    <p>Terminvereinbarung ist im Ausländeramt München möglich.</p>
    <p>Bitte besuchen Sie folgenden Link für mehr Informationen: <a href="https://stadt.muenchen.de/buergerservice/terminvereinbarung.html#/services/10339027/locations/10187259">Terminvereinbarung im Ausländeramt München</a></p>
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    print("email sent")
    
    

driver.quit()
