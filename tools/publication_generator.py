from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

with open('_Hua Chen_ - _Google Scholar_.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    publication_records = soup.find_all(class_="gsc_a_tr")
    # publication_record = publication_records[2]
    records_list = list()
    record_dict = dict()
    for publication_record in publication_records:
        try:
            publication_title = publication_record.find_all(class_="gsc_a_at")
            record_dict["title"] = publication_title[0].text
            record_dict["authors"] = publication_record.find_all(class_="gs_gray")[0].text
            record_dict["type"] = publication_record.find_all(class_="gs_gray")[1].text
            record_dict["year"] = publication_record.find(class_="gsc_a_y").text
            record_dict["url"] = publication_record.find(class_="gsc_a_at")["href"]
            records_list.append(record_dict.copy())
        except:
            pass
    
    # for i in range(len(records_list)):
    #     chrome_options = Options()
    #     chrome_options.add_argument('--headless') # Headless mode
    #     chrome_options.add_argument('--disable-gpu')
    #     driver = webdriver.Chrome(options=chrome_options)
    #     print(records_list[i]["url"])
    #     driver.get(records_list[i]["url"])
    #     time.sleep(1)
    #     page_source = driver.page_source
    #     driver.quit()
    #     # soup = BeautifulSoup(page_source, 'html.parser')
    #     print(soup)
    #     info = publication_record.find_all(class_="gs_scl")
    #     print(info)
    #     for data in info:
    #         key = data.find("gsc_oci_field").text
    #         value = data.find("gsc_oci_value").text
    #         records_list[i][key] = value
    #     break

    # print(records_list[0])


    # # for i in range(len(records_list)):
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    # }

    # response = requests.get("https://scholar.google.com/citations?hl=en&user=sFTLO0EAAAAJ", headers=headers)
    # print(response.status_code)
    # print(response.text)
            

        

    for i in range(len(records_list)):
        title_list = records_list[i]['title'].split(" ")
        abbrev = ""
        for word in title_list:
            abbrev += word[0].strip().lower()
        # print(abbrev)
        os.makedirs(f"{abbrev}", exist_ok=False)
        markdown_file = f"{abbrev}/_index.md"
        markdown_content = "---\n"
        markdown_content += f"title: '{records_list[i]['title']}'\n"
        markdown_content += "authors:\n"
        authors = records_list[i]["authors"].split(",")
        for author in authors:
            markdown_content += f"  - {author.strip()}\n"
        markdown_content += f"date: '{records_list[i]['year']}-01-01T00:00:00Z'\n"
        markdown_content += f"publication_types: ['0']\n"
        markdown_content += f"publication: '{records_list[i]['type']}'\n"
        markdown_content += f"feautured: false\n"
        markdown_content += "links:\n"
        markdown_content += f"  - name: 'Google Scholar'\n"
        markdown_content += f"    url: '{records_list[i]['url']}'\n"
        markdown_content += "projects:\n  - internal-project\n"
        markdown_content += "share: false\n"
        markdown_content += "---\n"
        with open(markdown_file, 'w', encoding='utf-8') as file:
            file.write(markdown_content)
        # break
    
    print(markdown_content)


    
