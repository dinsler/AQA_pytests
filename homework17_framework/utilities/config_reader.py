import configparser

from homework17_framework.constans import ROOT_DIR

abs_path = f'{ROOT_DIR}/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


def get_application_url():
    return config.get('app_data', 'app_url')


def get_user_creds():
    return (config.get('user_data', 'email'),
            config.get('user_data', 'password')
            )


def get_invalid_user_creds():
    return (config.get('invalid_user_data', 'email'),
            config.get('invalid_user_data', 'password'))


def get_browser_id():
    return config.get('browser_data', 'browser_id')


def get_search_item():
    return (config.get('search_data', 'search_item'),
            config.get('search_data', 'invalid_search_item')
            )


def get_review_data():
    return (config.get('review_data', 'username'),
            config.get('review_data', 'invalid_username')
            )


def get_invalid_discount_code():
    return config.get('discount_data', 'invalid_discount')
