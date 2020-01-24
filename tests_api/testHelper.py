import os
import json
import requests
from tests_api.config import URL_AUTH, AUTH_PAYLOADS, HEADER, URL_USERS,URL_EVENT


class Header:

    def get_header_auth_admin(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {
            "accept": "application/json",
            "Content-Type": "application/json-patch+json",
            "authorization": "Bearer " + auth}
        return header

    def get_header_auth_user(self):
        response_decoded_json = requests.post(URL_AUTH['url_login'], data=json.dumps(AUTH_PAYLOADS['payload_user']),
                                              headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {
            "accept": "application/json",
            "Content-Type": "application/json-patch+json",
            "authorization": "Bearer " + auth}
        return header

    def get_header_auth_vasya(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login'], data=json.dumps(
                AUTH_PAYLOADS['payload_vasya']), headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {
            "accept": "application/json",
            "Content-Type": "application/json-patch+json",
            "authorization": "Bearer " + auth}
        return header

    def get_token_admin(self):
        response_decoded_json = requests.post(URL_AUTH['url_login'], data=json.dumps(AUTH_PAYLOADS['payload_admin']),
                                              headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        token = "Bearer " + auth
        return token


class Event():

    CURRENT_PATH = os.path.abspath('CH_096_TAQC')

    header = {
        'Content-Type': 'multipart/form-data',
        'Authorization': Header().get_token_admin()
        }

    payload = {
        'Title': 'Test Event',
        'Description': 'Event for testing search',
        'DateFrom': 'Fra Jan 24 2020',
        'DateTo': 'Mon Feb 10 2020',
        'User.Id': 'f320932e-aac2-4999-32d3-08d79b47df59',
        'CityId': '418ad80a-85da-4033-f8df-08d79b47df2b',
        'Categories[0].Id': '60c56914-a974-4b4c-f461-08d79b47df60'
        }

    files = {
        #'Photo': open(os.path.join(CURRENT_PATH) + 'Data\\imageAddEvent\\testing_img.png','rb')
        }

    def create(self):
        response = requests.post(URL_EVENT['url_event_edit'], headers=self.header, data = self.payload, files = self.files)
        print(URL_EVENT['url_event_edit'], self.header, self.payload, self.files)
        print(response)



    def get_token_admin(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers=HEADER['header'])
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        token = "Bearer " + auth
        return token


class User:
    """Class to test Users API"""

    def __init__(
            self,
            id="05a469fe-8f90-479e-ed9a-08d7a0ce42ac",
            name='Vasya',
            gender=0,
            birthday="2000-01-01"):
        """Init new user data"""
        self.id = id
        self.name = name
        self.birthday = birthday + "T00:00:00"
        self.gender = gender
        self.payload_edit_gender = {
            "id": self.id,
            "gender": self.gender}
        self.payload_edit_birthday = {
            "id": self.id,
            "birthday": self.birthday}
        self.payload_edit_username = {
            "id": self.id,
            "name": self.name}

    def PAYLOAD_edit_gender(self):
        """Reload PAYLOAD_gender data"""
        PAYLOAD_edit_gender = {
            "id": self.id,
            "gender": self.gender}
        return PAYLOAD_edit_gender

    def PAYLOAD_edit_username(self):
        """Reload PAYLOAD_username data"""
        PAYLOAD_edit_username = {
            "id": self.id,
            "name": self.name}
        return PAYLOAD_edit_username

    def PAYLOAD_edit_birthday(self):
        """Reload PAYLOAD_birthday data"""
        PAYLOAD_edit_birthday = {
            "id": self.id,
            "birthday": self.birthday}
        return PAYLOAD_edit_birthday

    def edit_gender(self):
        """Edit user gender"""
        response_decoded_json = requests.post(
            URL_USERS['edit_gender'],
            data=json.dumps(
                self.payload_edit_gender),
            headers=Header().get_header_auth_vasya())
        print("Гендер змінено")

    def edit_username(self):
        """Edit user name"""
        response_decoded_json = requests.post(
            URL_USERS['edit_username'],
            data=json.dumps(
                self.payload_edit_username),
            headers=Header().get_header_auth_vasya())
        print("Ім'я змінено")
        return response_decoded_json

    def edit_birthday(self):
        """Edit user birthday"""
        response_decoded_json = requests.post(
            URL_USERS['edit_birthday'],
            data=json.dumps(
                self.payload_edit_birthday),
            headers=Header().get_header_auth_vasya())
        print("Дату відредаговано на ", self.birthday[:10])
        return response_decoded_json

    def back_username(self):
        """Return user name"""
        self.name = "Vasya"
        response_decoded_json = requests.post(
            URL_USERS['edit_username'],
            data=json.dumps(
                self.PAYLOAD_edit_username()),
            headers=Header().get_header_auth_vasya())
        print("Ім'я вернулось")
        return response_decoded_json

    def back_gender(self):
        """Return user data"""
        self.gender = 0
        response_decoded_json = requests.post(
            URL_USERS['edit_gender'],
            data=json.dumps(
                self.PAYLOAD_edit_gender()),
            headers=Header().get_header_auth_vasya())
        print("Гендер вернувся")
        return response_decoded_json

    def back_birthday(self):
        """Return user birthday"""
        self.birthday = "2000-01-01T00:00:00"
        response_decoded_json = requests.post(
            URL_USERS['edit_birthday'],
            data=json.dumps(
                self.PAYLOAD_edit_birthday()),
            headers=Header().get_header_auth_vasya())
        print("Дату повернено на ", self.birthday[:10])
        return response_decoded_json

    def get_info_by_id(self):
        """Get all user info by user-id"""
        response_decoded_json = requests.get(
            URL_USERS['user_by_id_vasya'],
            headers=Header().get_header_auth_vasya())
        Json = response_decoded_json.content.decode()
        dictionary = json.loads(Json)
        return dictionary

    def get_gender(self):
        """Get user gender"""
        dictionary = self.get_info_by_id()
        gender = dictionary["gender"]
        return gender

    def get_birthday(self):
        """Get user birthday"""
        dictionary = self.get_info_by_id()
        birthday = dictionary["birthday"]
        return birthday[:10]

    def get_username(self):
        """Get user username"""
        dictionary = self.get_info_by_id()
        birthday = dictionary["name"]
        return birthday

"""
id = "05a469fe-8f90-479e-ed9a-08d7a0ce42ac"
print(Header().get_token_admin())
user = User(id, "Jesus", 2, "2001-06-04")
print(user.get_info_by_id())
user.edit_username()
user.edit_gender()
user.edit_birthday()
print(user.get_info_by_id())
user.back_username()
user.back_gender()
user.back_birthday()
print(user.get_info_by_id())
"""