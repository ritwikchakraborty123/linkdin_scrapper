from selenium import webdriver
import os,random,sys,time
import bs4

username=input("Linkdin username/email : ")
password=input("Linkdin Password : ")


# have to set environment variable C:/chromedriver 
browser=webdriver.Chrome('C:/chromedriver/chromedriver.exe');


browser.get('https://www.linkedin.com/uas/login')

usernameId=browser.find_element_by_id('username');
passwordId=browser.find_element_by_id('password');

usernameId.send_keys(username);
passwordId.send_keys(password);

usernameId.submit();

# profileLink='https://www.linkedin.com/in/ritwik-chakraborty-6091951a0/'
# profileLink="https://www.linkedin.com/in/ianbremmer/"
profileLink=input("Link to Scrap : ")

browser.get(profileLink)
# bs4(browser.page_source)

SCROLL_PAUSE_TIME=5

last_height=browser.execute_script("return document.body.scrollHeight")

# while True:
# 	browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# 	time.sleep(SCROLL_PAUSE_TIME)
# 	new_height=browser.execute_script("document.body.scrollHeight")
# 	if(new_height==last_height):
# 		break;
# 	last_height=new_height

height=0

while True:
	browser.execute_script("window.scrollTo(0,"+str(height)+");")
	time.sleep(SCROLL_PAUSE_TIME)
	if(height>=last_height):
		break
	height+=800


# print(browser.page_source)
soup=bs4.BeautifulSoup(browser.page_source,'lxml')
name_class=soup.find("div",{"class":"flex-1 mr5"})
name_loc=name_class.find_all("ul")
name=name_loc[0].find("li").get_text().strip()
location=name_loc[1].find("li").get_text().strip()

title=name_class.find("h2").get_text().strip()

d=0
exp_section=soup.find("section",{"id":"experience-section"})
try:
	exp_section=exp_section.find("ul")
except:
	d=0

li_tags=[]
try:
	li_tags=exp_section.find_all("li")
except:
	d=0
print(" primary_info : ")
print(name)
print(location)
print(title)
company_name=""
duration=""
job_title=""
print("Job experience : ")
for i in li_tags:
	li_tag=i.find("div")
	a_tags=i.find("a")
	try:
		job_title=a_tags.find("h3").get_text().strip()
	except:
		d=0
	try:
		company_name=a_tags.find_all("p")[1].get_text().strip()
	except:
		d=0
	# try:
		# duration=a_tags.find_all("h4")[0].find_all("span")[1].get_text().strip()

	print(job_title)
	print(company_name)
	# print(duration)
	print(job_title)
	print("")

try:
	print("Educational part : ")
	edu_section=soup.find("section",{"id":"education-section"}).find("ul").find("li")
	college_name=edu_section.find("h3").get_text().strip()
	degree=edu_section.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find_all("span")[1].get_text().strip()
	stream=edu_section.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find_all("span")[1].get_text().strip()
	year=edu_section.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find_all("span")[1].get_text().strip()
except:
	d=0
print(college_name)
print(degree)
print(stream)
print(year)

#bs4(browser.page_source)
# submit=browser.find_element(By.CLASS,"btn__primary--large from__button--floating mercado-button--primary");
# submit.click();