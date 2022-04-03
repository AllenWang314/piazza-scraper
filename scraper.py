import time
from selenium import webdriver
import config
import requests
import re
from mdutils.mdutils import MdUtils
from mdutils import Html

driver = webdriver.Chrome() # selenium driver
PAGE_WAIT_TIME = 2 # wait time for loading

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text).replace('\n', ' ')
 
def get_data(driver, index):
    """Scrapes data from html page of post {index} with selenium {driver}"""
    driver.get(f'{config.URL}?cid={index}')
    time.sleep(PAGE_WAIT_TIME)
    post_body = driver.find_element_by_xpath('//*[@id="page_center"]/div[5]')
    elements = post_body.find_elements_by_tag_name("p")
    time.sleep(PAGE_WAIT_TIME)

    title = driver.find_element_by_xpath('//*[@id="view_quesiton_note"]/h1')
    
    question_p = (driver.find_element_by_xpath('//*[@id="questionText"]')
        .get_attribute('innerHTML')
    )
    student_p = (driver.find_element_by_xpath('//*[@id="member_answer"]')
        .find_elements_by_tag_name("p")
    )
    instructor_p = (driver.find_element_by_xpath('//*[@id="instructor_answer"]')
        .find_elements_by_tag_name("p")
    )
    tags = (driver.find_element_by_xpath('//*[@id="view_quesiton_note"]/div[2]')
        .find_elements_by_tag_name("a")
    )
    time.sleep(PAGE_WAIT_TIME)
   
    return {
        "title": title.text, 
        "question": remove_html_tags(str(question_p)),
        "student_answer": " ".join([p.text for p in student_p]),
        "instructor_answer": " ".join([p.text for p in instructor_p]),
        "tags": ", ".join([a.text for a in tags]),
        "index": index
    }

def main():
    """ 
        scrapes piazza posts with instructor and student answers up to post
        config.NUM_POSTS. prints invalid piazza post ids upon completion.
        saves posts to markdown file in output/
    """
    driver.get(config.URL)
    driver.implicitly_wait(PAGE_WAIT_TIME)

    # Log into account
    time.sleep(PAGE_WAIT_TIME)
    email = driver.find_element_by_xpath('//*[@id="email_field"]')
    kerberos.send_keys(config.EMAIL)
    password = driver.find_element_by_xpath('//*[@id="password_field"]')
    password.send_keys(config.PASSWORD)
    driver.find_element_by_xpath('//*[@id="modal_login_button"]').click()

    post_list = []
    invalid_ids = []
    for i in range(config.NUM_POSTS, 0, -1):
        try:
            post_list.append(get_data(driver, i))
        except Exception:
            invalid_ids.append(i)
    driver.quit()

    mdFile = MdUtils(file_name='piazza_posts', title='6.033 Piazza Posts')

    mdFile.new_paragraph("""This file includes all piazza posts scraped as of 
        noon 3/31. Only instructor and student answers have been included. 
        Followup discussion was omitted to keep things short and sweet.""")

    for post in post_list:
        mdFile.new_header(level=1, title=f'@{post["index"]} {post["title"]}')
        mdFile.write("- Question: " + post["question"] + "\n" + 
        "- Tags: " + post["tags"] + "\n" + 
        "- Students' Answer: " + post["student_answer"] + "\n" +
        "- Instructors' Answer: " + post["instructor_answer"])

    mdFile.create_md_file()
    print("invalid page ids", invalid_ids)

if __name__ == "__main__":
    main()