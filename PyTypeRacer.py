from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def num_there(s):
    return any(i.isdigit() for i in s)


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://play.typeracer.com/')
sleep(5)
#sc-bxivhb gUuNph
browser.find_element_by_css_selector('#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.sc-bxivhb.gUuNph').click()
sleep(2)
browser.find_element_by_css_selector('#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a').click()
sleep(5)
aa  = browser.find_elements_by_tag_name('''span''')
af = []
flag = 0
for i in aa:
    it = i.text
    print(it)
    if(len(it)>0 and not num_there(it) and it.find('Auto-updating') == -1 and it!='in' and not (it.startswith('(') and it.endswith(')'))):
        af.append(it)


asd = af[0]+(' '.join(af[1:]))
print(asd)
bbn = browser.find_element_by_class_name('txtInput')
sleep(10)
n=4
line = asd
khafanLi = [line[i:i+n] for i in range(0, len(line), n)]

for i in khafanLi:

    bbn.send_keys(i)
    sleep(0.5)


