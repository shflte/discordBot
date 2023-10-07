from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class XPATH:
    search_bar = "//input[@id='search']"
    solo_rank = "//div[.='單排積分']/following-sibling::div//div[@class='tier']"
    plays_list = "//div[@class='game-content']"
    result = "//div[@class='result']"
    # kda = "//div[@class='kda']"

class GAME:
    def __init__(self):
        self.result = ""
        self.kda = ""

def to_url_name(name: str):
    return name.replace(" ", "%20")

def init_driver(player: str) -> webdriver:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.op.gg/summoners/tw/" + to_url_name(player)
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, XPATH.solo_rank)))
    return driver

def get_rank(player: str) -> tuple:
    driver = init_driver(player)
    solo_rank = driver.find_element(By.XPATH, XPATH.solo_rank).text
    driver.quit()
    return (solo_rank.split(" ")[0], solo_rank.split(" ")[1])

def get_recent_plays(player: str) -> list:
    driver = init_driver(player)

if __name__ == "__main__":
    print(get_rank("你是什麼蛋餅"))




