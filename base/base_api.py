import requests
import json
import jsonpath as jsn


class BaseApi:

    def get_request(self, url, headers=None, params=None):
        """
        Use this method to send the get request
        :param url: The request URL
        :param params: The request params
        :param headers: The request headers
        :return: response
        """
        response = requests.get(url, params=params, headers=headers, verify=False)
        return response

    def post_request(self, url, json_data, headers=None):
        """
        Use this method to send the get request
        :param url: The request URL
        :param json_data: The request json_data
        :param headers:the request headers
        :return: response
        """
        response = requests.post(url, json_data, headers=headers, verify=False)
        return response

    def put_request(self, url, json_data, headers=None):
        """
        Use this method to send the put request
        :param headers: The request headers
        :param url: The request URL
        :param json_data: The request json data
        :return: response
        """
        response = requests.put(url, json_data, headers=headers, verify=False)
        return response

    def delete_request(self, url, headers=None):
        """
        Use this method to send the DELETE request
        :param url: The request URL
        :param headers:The request headers
        :return: response
        """
        response = requests.delete(url, headers=headers, verify=False)
        return response

    def check_status_code(self, response, expected_status_code):
        """
        Use this method to check the response status code
        :param response: response
        :param expected_status_code: expected status code
        """
        assert response.status_code == expected_status_code

    def get_json_value_by_key(self, response, key):
        """
        Returns list of values associated with a key
        :param response:
        :param key:
        :return: values_in_json
        """
        json_data = json.loads(response.text)
        values_in_json = jsn.jsonpath(json_data, key)
        return values_in_json

