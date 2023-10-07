from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

rank_chinese = {
    "IRON": "鐵",
    "BRONZE": "銅",
    "SILVER": "銀",
    "GOLD": "金",
    "EMERALD" : "翡翠",
    "PLATINUM": "鉑",
    "DIAMOND": "鑽",
    "MASTER": "大師",
    "GRANDMASTER": "宗師",
    "CHALLENGER": "挑戰者",
}

class XPATH:
    header_title = "//h2"
    search_bar = "//input[@id='search']"
    solo_rank = "//div[@id='content-container']//div[@class='tier']"
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
    wait.until(EC.presence_of_element_located((By.XPATH, XPATH.search_bar)))
    return driver

def check_player_exist(driver: webdriver) -> bool:
    header_title = driver.find_element(By.XPATH, XPATH.header_title).text
    return header_title != "This summoner is not registered at OP.GG. Please check spelling."

def get_rank(player: str) -> tuple:
    driver = init_driver(player)
    if not check_player_exist(driver):
        driver.quit()
        return ("", "")
    solo_rank = driver.find_element(By.XPATH, XPATH.solo_rank).text
    driver.quit()
    return (solo_rank.split(" ")[0], solo_rank.split(" ")[1])

def get_recent_plays(player: str) -> list:
    driver = init_driver(player)

if __name__ == "__main__":
    print(get_rank("這是誰這不是我我不是"))




