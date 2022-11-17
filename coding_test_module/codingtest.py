
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import requests
import pyperclip
from prettytable import PrettyTable

from bs4 import BeautifulSoup as bs
#from IPython.display import Javascript, display
from IPython.display import Javascript
from IPython import display

class boj:
    DRIVER = None
    BOJ_SESSION = None
    FILE_NAME = None

    def __init__(self, param):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--window-size=1,1")
        options.add_argument("--window-position=500,500")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.DRIVER = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
        #driver.set_window_position(500, 100, windowHandle='current')
        self.DRIVER.implicitly_wait(5)
        self.DRIVER.get('https://www.acmicpc.net/login?next=/')
        time.sleep(0.5)
        self.clipboard_input('login_user_id', param[0])
        time.sleep(1)
        self.clipboard_input('login_password', param[1])
        self.DRIVER.find_element(By.ID,'submit_button').click()
        time.sleep(0.5)
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        }
        ss = requests.session()
        ss.headers.update(headers)

        for cookie in self.DRIVER.get_cookies():
            c = {cookie['name']: cookie['value']}
            ss.cookies.update(c)
        self.BOJ_SESSION = ss

    def clipboard_input(self, tag_name, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장
        pyperclip.copy(user_input)
        self.DRIVER.find_element(By.NAME, tag_name).click()
        ActionChains(self.DRIVER).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(0.5)

    def 레벨별문제리스트(self, level, page):
        json_data = {
            "query":"solvable:true tier:"+level,
            "page":page,
        }
        res = requests.get("https://solved.ac/api/v3/search/problem",json_data)
        table = PrettyTable()
        table.title = '레벨별문제 '+ level
        table.field_names = ['문제번호_1','문제명_1','문제타입_1','문제번호_2', '문제명_2', '문제타입_2']
        table.align['문제번호_1'] = "l"
        table.align['문제명_1'] = "l"
        table.align['문제타입_1'] = "l"
        table.align['문제번호_2'] = "l"
        table.align['문제명_2'] = "l"
        table.align['문제타입_2'] = "l"

        add_item = []
        for item in res.json()['items']:
            add_item.append(item['problemId'])
            add_item.append(item['titleKo'])
            problem_type = []
            for in_item in item['tags']:
                for iin_item in in_item['displayNames']:
                    if iin_item['language']=='ko':
                        problem_type.append(iin_item['name'].strip()[:5])
            add_item.append(', '.join(problem_type)[:15])

            if len(add_item) == 6:
                table.add_row(add_item)
                add_item = []
        print(table)

    def 문제보기(self, problem):
        res = self.BOJ_SESSION.get('https://www.acmicpc.net/problem/'+problem)
        bs_html = bs(res.text,  "html.parser")
        self.FILE_NAME =bs_html.find('title').get_text()
        for item in bs_html.find_all('section', 'problem-section'):
            print(''.join( [ss.get_text() for ss in item.find_all('p')]))
            if item.select('tr'):
                for in_item in item.select('tr'):
                    print(in_item.get_text().strip().replace('\n', ''))
            if item.select('img'):
                img_src = item.find('img')['src']
                if img_src.startswith('https://'):
                    display.display(display.Image(img_src))
                else:
                    display.display(display.Image('https://www.acmicpc.net'+img_src))
                #https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/201003/dfcmhrjj_142c3w76qg8_b.jpg

        table = PrettyTable()
        table.title = '예제입력'
        table.field_names = ['예제입력_1','예제출력_1','예제입력_2','예제출력_2']
        table.align['예제입력_1'] = "l"
        table.align['예제출력_1'] = "l"
        table.align['예제입력_2'] = "l"
        table.align['예제출력_2'] = "l"
        add_item = []
        for item in bs_html.find_all('pre', class_='sampledata'):
            add_item.append(item.get_text().strip().replace('\r', ''))
            if len(add_item) == 4:
                table.add_row(add_item)
                add_item =[]

        if len(add_item) > 0:
            while True:
                if len(add_item) == 4:
                    table.add_row(add_item)
                    break
                add_item.append('-')
        print(table)

        # making srouce code
        src = '%%writefile ./boj/'+ self.FILE_NAME.replace(' ', '').replace(':','_') +'.py\n'
        src = src + '# 소스코드를 작성하는 공간입니다. 코딩을 하기 위해서는 writefile 라인을 주석처리해주세요\n'
        src = src + '# 주피터노트북에서는 입력시 input()을 사용하고 제출시 sys.stdin.readline() 으로 변경하세요~성능차이남\n'
        self.source_init(src)

    def source_init(self, src):
        with open('run_next_cell_patch.js') as f:
            # Monkey patch Jupyter with
            # set_next_input(run=True) functionality
            display.display(Javascript(f.read()))

        from IPython import get_ipython
        ip = get_ipython()
        ip.payload_manager.write_payload(
            dict(
                source='set_next_input',
                text=src,
                replace=False,
                execute=True
            )
        )


class leetcode:

    DRIVER = None
    LEET_SESSION = None

    def __init__(self, param):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.DRIVER = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
        self.DRIVER.implicitly_wait(5)
        self.DRIVER.get('https://leetcode.com/accounts/login/?next=/problemset/all/')
        time.sleep(0.5)
        self.clipboard_input('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/form/span[1]/input', param[0])
        self.clipboard_input('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/form/span[2]/input', param[1])
        self.DRIVER.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/button/div').click()
        time.sleep(0.5)
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        }
        ss = requests.session()
        ss.headers.update(headers)

        for cookie in self.DRIVER.get_cookies():
            c = {cookie['name']: cookie['value']}
            ss.cookies.update(c)
        self.LEET_SESSION = ss
        self.DRIVER.minimize_window()


    def clipboard_input(self, user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장
        pyperclip.copy(user_input)
        self.DRIVER.find_element(By.XPATH, user_xpath).click()
        ActionChains(self.DRIVER).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(0.5)

    def source_init(self, src):
        with open('run_next_cell_patch.js') as f:
            # Monkey patch Jupyter with
            # set_next_input(run=True) functionality
            display.display(Javascript(f.read()))

            from IPython import get_ipython
            ip = get_ipython()
            ip.payload_manager.write_payload(
                dict(
                    source='set_next_input',
                    text=src,
                    replace=False,
                    execute=True
                )
            )

    def get_session_from_site(self):
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        }
        ss = requests.session()
        ss.headers.update(headers)

        for cookie in self.DRIVER.get_cookies():
            c = {cookie['name']: cookie['value']}
            ss.cookies.update(c)
        self.LEET_SESSION = ss

    def getProblemListQueryJson(self, diffculty, size):
        query = """
            query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
          problemsetQuestionList: questionList(
            categorySlug: $categorySlug
            limit: $limit
            skip: $skip
            filters: $filters
          ) {
            total: totalNum
            questions: data {
              acRate
              difficulty
              freqBar
              frontendQuestionId: questionFrontendId
              isFavor
              paidOnly: isPaidOnly
              status
              title
              titleSlug
              topicTags {
                name
                id
                slug
              }
              hasSolution
              hasVideoSolution
            }
          }
        }
    """

        variables = {
            "categorySlug": "algorithms",
            "skip": 0,
            "limit": size,
            "filters": {
                "difficulty": diffculty,
                "status": "NOT_STARTED"
            }
        }

        return {'query': query, 'variables': variables}

    def getProblemText(self, res_data, language):
        print(res_data.json()['data']['question']['title'])

        for item in res_data.json()['data']['question']['topicTags']:
            print(item['name'], end=', ')

        print('')
        bs_html = bs(res_data.json()['data']['question']['content'], "html.parser")
        for line in bs_html:
            line_text = line.get_text().strip()
            if line_text != '':
                if 'Example' in line_text:
                    print('')
                print(line_text)

        # making srouce code
        src = '%%writefile ./leetcode/'+ res_data.json()['data']['question']['titleSlug'] +'.py\n'
        src = src + '# 소스코드를 작성하는 공간입니다. 코딩을 하기 위해서는 writefile 라인을 주석처리해주세요\n'
        for item in res_data.json()['data']['question']['codeSnippets']:
            if item['lang'] == language:
                src = src + item['code']+'\n'
                #print(item['code'])
        self.source_init(src)

    def getProblemQueryJson(self, problem):
        query = """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            boundTopicId
            title
            titleSlug
            content
            translatedTitle
            translatedContent
            isPaidOnly
            canSeeQuestion
            difficulty
            likes
            dislikes
            isLiked
            similarQuestions
            exampleTestcases
            categoryTitle
            contributors {
              username
              profileUrl
              avatarUrl
              __typename
            }
            topicTags {
              name
              slug
              translatedName
              __typename
            }
            companyTagStats
            codeSnippets {
              lang
              langSlug
              code
              __typename
            }
            stats
            hints
            solution {
              id
              canSeeDetail
              paidOnly
              hasVideoSolution
              paidOnlyVideo
              __typename
            }
            status
            sampleTestCase
            metaData
            judgerAvailable
            judgeType
            mysqlSchemas
            enableRunCode
            enableTestMode
            enableDebugger
            envInfo
            libraryUrl
            adminUrl
            challengeQuestion {
              id
              date
              incompleteChallengeCount
              streakCount
              type
              __typename
            }
            __typename
          }
        }
        """
        variables = {"titleSlug": problem}
        return {'query': query, 'variables': variables}

    def getSubmissionsQueryJson(self, problem):
        operationName = "Submissions"
        query = """
            query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {
          submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {
            lastKey
            hasNext
            submissions {
              id
              statusDisplay
              lang
              runtime
              timestamp
              url
              isPending
              memory
              __typename
            }
            __typename
          }
        }
    """
        variables = {
            "offset": 0,
            "limit": 20,
            "lastKey": None,
            "questionSlug": problem
        }

        return {'operationName' :operationName, 'query': query, 'variables': variables}

    def 문제리스트(self, diffculty, size=5):
        res = self.LEET_SESSION.post('https://leetcode.com/graphql', json=self.getProblemListQueryJson(diffculty, 50))
        #question_id = res.json()['data']['problemsetQuestionList']['questions'][0]['frontendQuestionId']
        #file_name = res.json()['data']['problemsetQuestionList']['questions'][0]['titleSlug']
        for i in range(size):
            print(res.json()['data']['problemsetQuestionList']['questions'][i]['frontendQuestionId'], end='. ')
            print(res.json()['data']['problemsetQuestionList']['questions'][i]['title'])
            print(res.json()['data']['problemsetQuestionList']['questions'][i]['titleSlug'])

    def 문제선택(self, problem, language='Python3'):
        res = requests.post('https://leetcode.com/graphql', json=self.getProblemQueryJson(problem))
        self.DRIVER.get('https://leetcode.com/problems/'+problem+'/')
        self.getProblemText(res, language)

    def 제출하기(self, problem):
        # submit 전에는 파일을 꼭 저장해주세요. 파일을 읽어서 서브밋을 날립니다.
        # set scource code pytho
        # 2 : java , 4 : python3   13 rust
        self.DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[1]/div[1]/div/div/div').click()
        time.sleep(0.5)
        try:
            self.DRIVER.find_element(By.XPATH, '/html/body/div[6]/div/div/div/ul/li[4]').click()
        except:
            self.DRIVER.find_element(By.XPATH, '/html/body/div[7]/div/div/div/ul/li[4]').click()
        source_input_xpath = "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[6]/div[1]/div/div"
        source_code = ''
        with open('./leetcode/'+problem+'.py', encoding='utf-8') as f:
            source_code = ''.join(f.readlines())
        self.clipboard_input(source_input_xpath, source_code)
        self.DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/div[2]/div/button').click()

    def 결과보기(self, problem):
        # get result
        res = self.LEET_SESSION.post('https://leetcode.com/graphql', json=self.getSubmissionsQueryJson(problem))
        print(res.json()['data']['submissionList']['submissions'][0])