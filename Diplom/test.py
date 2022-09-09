from page_objects import MainPage

def test_start_page(browser):
    MainPage(browser).login()
    MainPage(browser).page_switching()
    MainPage(browser).create_project()
    MainPage(browser).filling_out_report()