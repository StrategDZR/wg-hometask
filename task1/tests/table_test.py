import pytest
from selenium.webdriver.common.by import By

from task1.pages.TablePage import TablePage

url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'


@pytest.mark.parametrize("test_input", [1 * pow(10, 7),
                                        1.5 * pow(10, 7),
                                        5 * pow(10, 7),
                                        1 * pow(10, 8),
                                        5 * pow(10, 8),
                                        1 * pow(10, 9),
                                        1.5 * pow(10, 9),
                                        ])
def test_popularity(base_test, test_input):
    browser = pytest.browser
    sites_with_popularity_less_than_provided = []
    error_message = ""

    browser.get(url)
    rows = browser.find_elements(By.XPATH, TablePage.rows_locator)
    for row in rows:
        site_info = TablePage.get_site_info(row)
        if site_info.popularity < test_input:
            sites_with_popularity_less_than_provided.append(site_info)
            error_message += format(
                f"{site_info.name} (Frontend:{site_info.frontend}|Backend:{site_info.backend}) has "
                f"{site_info.popularity} unique visitors per month. (Expected more than {test_input})\n")

    assert len(sites_with_popularity_less_than_provided) == 0, error_message
