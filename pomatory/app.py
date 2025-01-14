import sys
import logging
import argparse
from selenium import webdriver
from setup_logger import logger

driver = webdriver


def set_up_webdriver(args=None):
    logger.info("Starting set up of webdriver")
    global driver

    if args.browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--remote-debugging-port=9222')
        driver = webdriver.Chrome(options=chrome_options)

    elif args.browser == 'firefox':
        driver = webdriver.Firefox()
    # TODO: add later
    # elif preferred_browser == 'edge':
    #     driver = webdriver.Edge()
    else:
        logging.error("Please provide one of the supported browsers. Options: chrome, firefox")

    driver.set_page_load_timeout(20)
    driver.implicitly_wait(5)
    driver.get(str(args.base_url))
    driver.maximize_window()

    # if request.cls is not None:
    #     request.cls.driver = driver
    #     request.cls.logger = logging

    # yield driver
    #
    # # cleaning up after the test suite run
    # driver.quit()


def main():
    parser = argparse.ArgumentParser(description='Welcome to POMatory!'
                                                 ' A tool to help you automate the boring work of locating '
                                                 'elements in a web page for your Automation Framework according'
                                                 ' to the POM architecture')
    parser.add_argument('-t', '--types',
                        dest='html_element_to_look_for_ids',
                        default=['input', 'button'],
                        help='Types of html elements to look for. '
                        )
    parser.add_argument('--url',
                        dest='base_url',
                        help='URL to start looking for locators.',
                        type=str
                        )
    parser.add_argument('-b', '--browser',
                        dest='browser',
                        help='Browser to use for the selenium navigation. '
                             'Available options: chrome, firefox. '
                             'default: firefox',
                        default="firefox",
                        type=str
                        )
    parser.add_argument('-u', '--username',
                        dest='username',
                        help='[Optional] Username to login. ',
                        type=str
                        )
    parser.add_argument('-p', '--password',
                        dest='password',
                        help='[Optional] Password to login. ',
                        type=str
                        )
    parser.add_argument('-w', '--web_driver',
                        dest='web_driver_download',
                        help='Whether to try to download the appropriate webdriver for the specified browser. '
                             'default: False',
                        default=False,
                        type=bool
                        )
    # TODO: Below are future improvements
    parser.add_argument('-v', '--verbose',
                        dest='verbose',
                        default=False,
                        help='Verbose Output. '
                             'default: False.'
                        )
    parser.add_argument('-q', '--quiet',
                        dest='quiet',
                        default=False,
                        help='Suppress Output. '
                             'default: False.'
                        )

    run(parser.parse_args())


def clean_up():
    global driver
    driver.quit()


def run(args):
    logger.info("test")
    set_up_webdriver(args=args)
    logger.info(f'The host is "{args.base_url}"')
    clean_up()


if __name__ == "__main__":
    sys.exit(main())
