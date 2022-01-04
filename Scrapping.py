import requests
from bs4 import BeautifulSoup

Website_to_scrap = [
    {
        "Website_URL": "https://www.flipkart.com/",
        "name": "Flipkart's",
    },
    {
        "Website_URL": "https://www.infinitiresearch.com/contact-us/",
        "name": "infinitiresearch's",
    },

    {
        "Website_URL": "https://www.tcs.com/about-us",
        "name": "TCS's",
    },

]


def give_me_data(URL):
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    if(URL=="https://www.flipkart.com/"):
        data = soup.find("div", {'class': "_2NKhZn _1U1qnR"})
        return data.getText()
    if (URL == "https://www.infinitiresearch.com/contact-us/"):
        data = soup.find("h4", {'class': "et_pb_module_header"})
        return data.getText()
    if (URL == "https://www.tcs.com/about-us"):
        data = soup.find("div", {'class': "menu-item-heading-connect"})
        return data.getText()


try:
    for every_website in Website_to_scrap:
        Data = give_me_data(every_website.get("Website_URL"))
        print(f"{every_website.get('name')} data:")
        print(Data)
finally:
    print("Success")
