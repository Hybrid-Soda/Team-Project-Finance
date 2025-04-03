### 크롤링 관련 ###
# 1. 브라우저 인스턴스를 생성하고 제어
# 2. Chrome 브라우저의 실행 옵션을 설정하는 데 사용
# 3. Selenium에서 웹 요소를 찾는 데 사용되는 위치 전략을 정의 (웹 요소 지정)
# 4. 지정한 윈도우나 탭을 찾을 수 없을 때 발생하는 예외 처리
from selenium import webdriver  # 1
from selenium.webdriver.chrome.options import Options  # 2
from selenium.webdriver.common.by import By  # 3
from selenium.common.exceptions import (
    NoSuchWindowException,
    NoSuchElementException,
)  # 4
import csv
import pandas as pd
from sqlalchemy import create_engine


# 드라이버 초기화
def configure_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--start-maximized")
    options.add_argument("disable-infobars")
    return webdriver.Chrome(options=options)


# CSV 파일 생성 (저장 경로, 쓰기 모드, 인코딩, 줄바꿈 없음으로 조정)
def open_csv_writers(static_dir="cards/"):
    card_file = open(f"{static_dir}/card_data.csv", "w", encoding="CP949", newline="")
    benefit_file = open(f"{static_dir}/benefit_data.csv", "w", encoding="CP949", newline="")

    card_writer = csv.writer(card_file)
    benefit_writer = csv.writer(benefit_file)

    card_writer.writerow(["pk", "name", "brand", "image", "annual_fee1", "annual_fee2", "record", "type"])
    benefit_writer.writerow(["card", "title", "content"])

    return card_writer, benefit_writer, card_file, benefit_file


def is_inactive_card(driver, card_url_selector):
    try:
        driver.find_element(By.CSS_SELECTOR, f"{card_url_selector} > div.data_area > div.btn_wrap > div.app_btn > a.inactive > span > b")
        return True
    except NoSuchElementException:
        return False


def extract_card_info(driver, card_url_selector):
    try:
        name = driver.find_element(By.CSS_SELECTOR, f"{card_url_selector} > div.data_area > div.tit > strong").text  # 이름
        brand = driver.find_element(By.CSS_SELECTOR, f"{card_url_selector} > div.data_area > div.tit > p").text  # 브랜드
        image = driver.find_element(By.CSS_SELECTOR, f"{card_url_selector} > div.plate_area > div.card_img > img").get_attribute("src")  # 이미지
        annual_fee1 = driver.find_element(By.CSS_SELECTOR, f"{card_url_selector} > div.bnf2 > dl:nth-child(1) > dd.in_out > span:nth-child(1) > b").text.replace(",", "").replace("원", "")  # 연회비 1
        record = driver.find_element(By.CSS_SELECTOR, f"{card_url_selector} > div.bnf2 > dl:nth-child(2) > dd > b").text.replace(",", "").replace("원", "")  # 전월 실적

        try:
            annual_fee2 = driver.find_element(By.CSS_SELECTOR, f"{card_url_selector} > div.bnf2 > dl:nth-child(1) > dd.in_out > span:nth-child(2) > b").text.replace(",", "").replace("원", "")  # 연회비 2
        except NoSuchElementException:
            annual_fee2 = None

        try:
            card_type = driver.find_element(By.CSS_SELECTOR, f"{card_url_selector} > div.bnf2 > dl:nth-child(3) > dd > span").text  # 타입입
        except NoSuchWindowException:
            card_type = None

        return [name, brand, image, annual_fee1, annual_fee2, record, card_type]

    except Exception as e:
        return None


def extract_card_benefits(driver, benefit_selector):
    benefit_name_elements = driver.find_elements(By.CSS_SELECTOR, f"{benefit_selector} > dt > p")
    benefit_content_elements = driver.find_elements(By.CSS_SELECTOR, f"{benefit_selector} > dt > i")

    benefits = []
    for name_el, content_el in zip(benefit_name_elements, benefit_content_elements):
        benefits.append((name_el.text, content_el.text))
    return benefits


def crawl_card_detail(driver, idx, pk, card_writer, benefit_writer):
    CARD_URL = "#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div"
    BENEFIT_URL = "#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.bene_area > dl"

    driver.get(f"https://www.card-gorilla.com/card/detail/{idx}")
    driver.execute_script('document.querySelector("#q-app > header").style.visibility="hidden";')

    if is_inactive_card(driver, CARD_URL):
        return pk

    card_info = extract_card_info(driver, CARD_URL)
    if not card_info:
        return pk

    card_writer.writerow([pk] + card_info)

    benefits = extract_card_benefits(driver, BENEFIT_URL)
    for bnf_title, bnf_content in benefits:
        benefit_writer.writerow([pk, bnf_title, bnf_content])

    return pk + 1