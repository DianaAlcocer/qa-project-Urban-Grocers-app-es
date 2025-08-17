import configuration
import data
import requests


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.user_header
                         )


def post_new_client_kit(kit_body, kit_header):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=kit_header
                         )
