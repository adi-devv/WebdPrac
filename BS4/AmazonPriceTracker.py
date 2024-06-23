import requests
from pprint import pprint
from bs4 import BeautifulSoup

headers = {
}
resp = requests.get(
    "https://www.amazon.in/Destinio-Large-Umbrella-Women-Close/dp/B089GM5Q7Z/ref=sr_1_1_sspa?crid=10EC0FF59RVPT&dib=eyJ2IjoiMSJ9.yXVjmlQj0rz3sD2xAN3W-pGYR8zT2RfAcfu_qV9X-LVfXfWKlR2zrM0ay6beZ0VzlbSqfriBf0hBwlvPZ4onXDM1ZfwYqfeN5zxMrHwb-XSQxJ_vFakpei_WdH-lpzV31hlvnSc917HJM5bgjoAHBVIPOhbFM0vXBtuZx0WSkjZ3rdJulCu8oUeT077iO5KTWZ7lv0QYJ9OBNb--2VI_YYvU69QyClSDBwTS7dFh0fOCkv7yHIvwH8a3KKz1b0Df9CxNPqDwnL7-kvXYVDGeyz4VhIYeWS3uu9l-6Xdr_sA.UtXQDnI1KuV6mBD14hXlcjUuOs4Z2IPLN_p-vfVh7bI&dib_tag=se&keywords=umbrella&qid=1719049950&sprefix=umre%2Caps%2C327&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
    headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')
pprint(resp.text)
price = soup.select('span.a-price-whole')
print(price)
