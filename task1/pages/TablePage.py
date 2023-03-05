from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from task1.dataclasses.WebsiteInfo import WebsiteInfo
from task1.utils.utils import clean_str_for_int, clean_str_for_str


class TablePage(object):
    rows_locator = '//caption[contains(text(), "Programming languages used in most popular websites*")]' \
                   '/parent::table/tbody/tr'
    website_locator = 'td[1]'
    popularity_locator = 'td[2]'
    frontend_locator = 'td[3]'
    backend_locator = 'td[4]'

    @classmethod
    def get_site_info(cls, row):
        if isinstance(row, WebElement):
            name = clean_str_for_str(row.find_element(By.XPATH, TablePage.website_locator).text)
            popularity = int(clean_str_for_int(row.find_element(By.XPATH, TablePage.popularity_locator).text))
            frontend = clean_str_for_str(row.find_element(By.XPATH, TablePage.frontend_locator).text)
            backend = clean_str_for_str(row.find_element(By.XPATH, TablePage.backend_locator).text)
            return WebsiteInfo(name, popularity, frontend, backend)
