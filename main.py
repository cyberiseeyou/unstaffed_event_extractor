from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup WebDriver ---
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

# --- Step 1: Login ---
driver.get("https://crossmark.mvretail.com")

wait.until(EC.presence_of_element_located((By.ID, "usernameInput"))).send_keys("mat.conder8135")
driver.find_element(By.ID, "passwordInput").send_keys("Password123!")
driver.find_element(By.ID, "standardLoginSubmitButton").click()

# --- Step 2: Click 'Planning' Tab ---
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-planning"]'))).click()

# --- Step 3: Click Conditions Dropdown and Select 'Unstaffed' ---
wait.until(EC.element_to_be_clickable((By.ID, "ext-gen1169"))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div/div[4]"))).click()

# --- Step 4: Type 'core' into Search Input ---
search_input = wait.until(EC.presence_of_element_located((By.ID, "planningsearch-inputEl")))
search_input.clear()
search_input.send_keys("core")

# --- Step 5: Click 'Add Filter' Button ---
wait.until(EC.element_to_be_clickable((By.ID, "planningaddsearchfieldbutton-btnWrap"))).click()

# --- Step 6: Click 'Search' Button ---
wait.until(EC.element_to_be_clickable((By.ID, "planningexecutesearchbutton"))).click()

# --- Step 7: Wait for Data to Load (wait for Download button to appear) ---
wait.until(EC.presence_of_element_located((By.ID, "downloadRepCsv-btnInnerEl")))

# --- Step 8: Click 'Download CSV' ---
wait.until(EC.element_to_be_clickable((By.ID, "downloadRepCsv-btnInnerEl"))).click()

# Optional: Wait to ensure download completes
time.sleep(5)

# --- Close Browser ---
driver.quit()

