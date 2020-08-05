from .constant import *
from malclient.client import Auth


class ForumApi(Auth):
    def forum_boards(self) -> dict:
        """
        function for get forum boards api
        :return:forum boards
        """
        url_endpoint = 'forum/boards'

        parameters = {}

        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)

    def topic_details(self, topic_id: int, limit: int = 10, offset: int = 0) -> dict:
        """
        function for get forum topic details api
        :param topic_id:id of forum topic
        :param limit:number of results user want default = 10
        :param offset: from where result should start from default = 0
        :return: details of forum topic of given topic id
        """
        url_endpoint = 'forum/topic/{}'.format(topic_id)
        parameters = {'limit': limit,
                      'offset': offset}
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)

    def forum_topics(self, board_id: int, subboard_id: int, topic: str, topic_user_name: str, user_name: str,
                     limit: int = 10, offset: int = 0, sort: int = "recent") -> dict:
        """
        function for get forum topics api
        :param board_id:board id
        :param subboard_id:subboard id
        :param topic:query string
        :param topic_user_name:query string
        :param user_name:query string
        :param limit:number of results user want default = 10
        :param offset: from where result should start from default = 0
        :param sort:currently only recent can be set
        :return:forum topics
        """
        url_endpoint = 'forum/topics'
        parameters = {'board_id': board_id,
                      subboard_id: subboard_id,
                      'q': topic,
                      'topic_user_name': topic_user_name,
                      'user_name': user_name,
                      'limit': limit,
                      'offset': offset,
                      'sort': sort}
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)
