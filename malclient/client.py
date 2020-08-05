import requests
import json

class Auth:
    """
    Main class through which user can access all the different api functions
    """
    def __init__(self, access_token, refresh_token, client_id, client_secret):
        """
        initialising the main class

        :param access_token: your access token
        :param refresh_token: your refresh token
        :param client_id: your apps client id
        :param client_secret: your apps client secret
        """
        self.url = "https://api.myanimelist.net/v2/"
        self.client_secret = client_secret
        self.client_id = client_id
        self.parms = {}
        self.access_token = access_token
        self.refresh_token = refresh_token

    @property
    def headers(self):

        head = 'Bearer {}'.format(self.access_token)
        return {'Authorization': head}

    def refreshed_token(self):
        """
        function which will get new access token so user don't have
        to get refresh token everytime the access token expire

        """
        url_endpoint = 'https://myanimelist.net/v1/oauth2/token'
        parameters = {'grant_type': 'refresh_token',
                      'refresh_token': self.refresh_token,
                      'client_id': self.client_id,
                      'client_secret': self.client_secret}
        result = requests.post(url=url_endpoint, data=parameters)
        self.access_token = result.content['access_token']
        self.refresh_token = result.content['refresh_token']

    def get_response(self, url, method, parameters):
        """
        function to call api

        """
        apiurl = 'https://api.myanimelist.net/v2/'
        version = 'v2/'

        url_endpoint = apiurl+url
        pars = parameters  # just for ref
        try:
            if method == "GET":
                response = requests.get(
                    url=url_endpoint, params=pars, headers=self.headers)

            elif method == "DELETE":
                response = requests.delete(url=url_endpoint, headers=self.headers)

            else:
                # right now myanimelist have only 3 types of api
                response = requests.patch(
                    url=url_endpoint, data=pars, headers=self.headers)

            result = json.loads(response.text)
            if response.status_code == 401 :
               if 'expired' in result.get('error') :
                    self.refreshed_token()
                    return self.get_response(url ,method,parameters)
               else:
                   return result
            else:
                return result
        except:
            print("wrong parameters")