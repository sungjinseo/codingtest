import time
import requests
import pyperclip

from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

PLAYGROUND = []
PLAY = 'playground/'
INSERT = '/insert.do?'
LOGIN = ''

def init_info(playgr):

    if '도곡' == playgr:
        PLAYGROUND = ['https://www.gangnam.go.kr/resv/apply/memewe_clean_playground/list.do?mid=ID04_02071902',]
    elif '세곡' == playgr:
        PLAYGROUND = ['https://www.gangnam.go.kr/resv/apply/segok_indoor_playground/list.do?mid=ID04_04070903','https://www.gangnam.go.kr/resv/reqst/segok_indoor_playground//insert.do?']
    elif '일원' == playgr:
        PLAYGROUND = ['https://www.gangnam.go.kr/resv/apply/irwon_playground/list.do?mid=ID04_04074703',]

    LOGIN = 'https://www.gangnam.go.kr/login.do?mid=ID91_9101&returnUrl='+PLAYGROUND[0][PLAYGROUND[0].index('go.kr')+5:]


def clipboard_input(user_xpath, user_input):
    temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

    pyperclip.copy(user_input)
    driver.find_element(By.XPATH, user_xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
    time.sleep(0.5)

def naver_and_gannam_login(login_id, loging_pass):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
    driver.implicitly_wait(5)
    driver.get('https://nid.naver.com/nidlogin.login')

    # 아이디와 비밀번호를 입력합니다.
    time.sleep(0.5) ## 0.5초
    clipboard_input('//*[@id="id"]', login_id)
    clipboard_input('//*[@id="pw"]', loging_pass)
    driver.find_element(By.XPATH, '//*[@id="log.login"]').click()

    driver.get(LOGIN)
    driver.find_element(By.XPATH, '//*[@id="contents-wrap"]/div[1]/div/div/div/div[1]/div[2]/div/div/ul/li[1]/button').click()

    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    ss = requests.session()
    ss.headers.update(headers)

    for cookie in driver.get_cookies():
        c = {cookie['name']: cookie['value']}
        ss.cookies.update(c)
    driver.quit()
    return ss

def getReservationList(ss):
    res = ss.get(PLAYGROUND[0])
    reserve = bs(res.text, "html.parser")
    table = [['날짜','예약시간','예약번호','예약시간','예약번호','예약시간','예약번호']]
    for item in reserve.find_all("td"):
        add_item = []
        if item.find('div', 'fc-sat') != None or item.find('div', 'holiday-color') != None:
            #주말
            #print(item.select_one('span').get_text(), '일')
            #for link in item.select('a'):
            #    print(link.get_text().strip(), link['href'][link['href'].find('playground/')+len('playground/'):link['href'].find('/add.do')])
            pass
        else:
            #평일
            add_item.append(item.select_one('span').get_text()+'일')
            for link in item.select('a'):
                add_item.append(link.get_text().strip())
                add_item.append(link['href'][link['href'].find('playground/')+len('playground/'):link['href'].find('/add.do')])
        if len(add_item) > 1 : table.append(add_item)

    return tabulate(table)

def addReservation(ss, reserve_num, rar_user_name,rar_hp_no,rar_person_cnt,rar_optn_values1, rar_optn_value2):
    REQ_STR = []
    REQ_STR.extend(PLAYGROUND[1][:PLAYGROUND[1].index(PLAY)+len(PLAY)] + reserve_num + PLAYGROUND[1][PLAYGROUND[1].index(INSERT):])
    REQ_STR.extend(PLAYGROUND[0][PLAYGROUND[0].index('mid='):])
    REQ_STR.extend('&rar_user_name='+rar_user_name+'&rar_hp_no='+rar_hp_no+'&rar_person_cnt='+rar_person_cnt)
    REQ_STR.extend('&rar_optn_keys=1&rar_optn_values='+rar_optn_values1+'&rar_optn_keys=2&rar_optn_values='+rar_optn_value2)
    REQ_STR.extend('&rar_reqst_key=0&rar_file_key=&rar_sms_yn=Y&rar_agree_yn=Y&rar_terms_yn=Y')

    result = ss.post(''.join(REQ_STR))
    return result

def checkReservation(ss):
    confirm_table = [['순번,','예약일시','취소번호','신청자명','휴대폰번호','신청인원','신청인원','상태','등록일', '취소번호']]
    res_list = ss.post(PLAYGROUND[0].replace('apply', 'reqst'))
    confirm_list = bs(res_list.text, "html.parser")
    for item in confirm_list.find_all('tr')[1:]:
        add_item = []
        for detail in item.find_all('td'):
            if len(detail.select('a'))>0 :
                cancel_str = str(detail.select('a')[0])
                cancel_str = cancel_str[cancel_str.index('playground/')+11:cancel_str.index('/view.do')]
                add_item.append(cancel_str)
            add_item.append(detail.text.strip())
        confirm_table.append(add_item)

    return tabulate(confirm_table)

def cancelReservation(ss, cancel_num):
    REQ_STR = []
    REQ_STR.extend(PLAYGROUND[1][:PLAYGROUND[1].index(PLAY)+len(PLAY)] + cancel_num + '/cancel.do?')
    REQ_STR.extend(PLAYGROUND[0][PLAYGROUND[0].index('mid='):])

    result = ss.post(''.join(REQ_STR))

if __name__ == '__main__':
    start = time.time()

    end = time.time()
    #print('걸린시간 : ', end - start)