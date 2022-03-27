from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://in.indeed.com/Openings-Bangalore-Only-jobs"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div',class_ = "job_seen_beacon")

salary = ''

with open('jobs.csv', 'w', newline='' ,encoding='utf8') as f:
    thewriter = writer(f)
    header = ['Title', 'Company', 'Salary']
    thewriter.writerow(header)
    
    for result in results :
        title = result.find('h2', class_ = "jobTitle").text.replace('\n','')
        company = result.find('span', class_ = "companyName").text.replace('\n','')
        salary1 = result.find('div',class_ = "metadata salary-snippet-container")
        if salary1:
            salary = salary1.text.replace('\n','')
        else:
            salary = 'Not mentioned'
        
        job_info = [title,company, salary]
        thewriter.writerow(job_info)