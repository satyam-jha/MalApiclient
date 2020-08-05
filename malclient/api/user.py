from .constant import *
from malclient.client import Auth



class UserApi(Auth):

    def user_info(self, user_field="name"):
        url_endpoint = 'users/@me'

        parameters = {'fields': user_field}
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)
