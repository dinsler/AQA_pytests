"""
Find web page.
Write 30 XPATH locators for this page using XPath Axes and Wildcards. Some of them should have more than 3 steps.
For 10 XPATH locators write 10 CSS locators which find the same element
"""

# url = https://www.instagram.com/  English language should be chosen

# 30 XPATH locators
login_form_xpath = '//*[@id="loginForm"]'
username_xpath = '//input[@name="username"]'
contact_xpath = '//section/child::footer//div/a[@tabindex="0" and @target="_blank"]'
logo_xpath = '//*[@aria-label="Instagram"]'
password_label_xpath = '//input[@name="password"]/ancestor::label'
get_the_app_xpath = '//*[text()="Get the app."]'
main_xpath ='//*[@class="_ab1y"]/../parent::main'
dont_have_account_xpath = '//*[contains(text(), "account?")]'
or_xpath = '//form/child::div/child::div[@class="_ab39"]'
login_button_xpath = '//form//div/div/button[contains(@type,"submit")]'
login_with_facebook_button_xpath = '//button[contains(@type,"button")]'
select_english_language_xpath = '//div/span//select/option[@value="en"]'
meta_xpath = '//a[@href="https://about.meta.com/"]'
girl_with_cat_img_xpath = '//article//div/div/img[@src="/images/instagram/xig/homepage/screenshots/screenshot1-2x.png?__d=www"]'
about_instagram_xpath = '//footer//div/a[@href="https://about.instagram.com/"]'
sign_up_xpath = '//p/child::a[contains(@href, "/accounts/emailsignup")]'
reset_password_xpath = '//form/a[contains(@href, "/accounts/password/reset/")]'
app_store_download_xpath = '//article//div[@class="_aa4v"]/a[@aria-label="Download on the App Store"]'
google_play_download_xpath = '//article//div[@class="_aa4v"]/a[@aria-label="Get it on Google Play"]'
page_footer_xpath = '//html/body//footer'
instagram_blog_xpath = '//html//body//footer//div/a[@href="https://about.instagram.com/blog/"]'
jobs_xpath = '//footer[contains(@role,"contentinfo")]//descendant::div//div/descendant::a[contains(@href,"/about/jobs/")]'
locations_xpath = '//footer//a[@role="link"]/*[text()="Locations"]'
api_xpath = '//div//child::footer//div/a[@rel="nofollow noopener noreferrer"]/div[text()="API"]'
copyright_xpath = '//*[contains(text(), "from Meta")]'
meta_verified_xpath = '//div//child::footer//div/a[@rel="nofollow noopener noreferrer"]/div[contains(text(), "Verified")]'
app_store_download_img_xpath = '//section//child::article//a/img[@alt="Download on the App Store"]'
google_play_download_img_xpath = '//section//child::article//a/img[@alt="Get it on Google Play"]'
help_xpath = '//section//child::footer//div/a/div[text()="Help"]'
top_accounts_xpath = '//body//footer//div/a[contains(@href, "/directory/profiles")]'
instagram_lite_xpath = '//footer//div/a[@role="link" and @tabindex="0"]/div[text()="Instagram Lite"]'

# 10 CSS locators
login_form_css = '#loginForm'
sign_up_css = 'a[href*="signup"]'
app_store_download_css = 'a[aria-label="Download on the App Store"]'
dont_have_account_css = '._ab25'
username_css = 'input[name="username"]'
page_footer_css = ':root body footer'
reset_password_css = 'form a[href*="reset"]'
main_css = '[role="main"]'
login_button_css = 'button[type="submit"]'
logo_css = '*[aria-label="Instagram"]'
