from playwright.sync_api import Page, expect
import re

def test_get_title(page: Page):
    page.goto("https://playwright.dev/")
    title = "Fast and reliable end-to-end testing for modern web apps | Playwright"
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page).to_have_title(title)
    assert title == page.title()
    print(page.title())

    get_started = page.get_by_role("link", name="Get Started")
    get_started.click()


