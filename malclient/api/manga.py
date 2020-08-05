from .constant import *
from malclient.client import Auth


class MangaApi(Auth):
    def search_manga(self, manga_name: str, limit: int = 10, offset: int = 0, fields: list = ('name', 'id')) -> dict:
        """
        function for search manga api
        :param manga_name:query string
        :param limit:number of results user want default = 10
        :param offset: from where result should start from default = 0
        :param fields: fields which user want to get
        :return:result for the query
        """
        url_endpoint = 'manga'
        field = ",".join(fields)

        parameters = {'q': manga_name,
                      'limit': limit,
                      'offset': offset,
                      'fields': field}
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)

    def get_manga_details(self, manga_id: int, fields: list = ('id', 'title', 'main_picture')) -> dict:
        """
        function for get manga details api
        :param manga_id:id of manga
        :param fields: fields which user want to get
        :return:details of manga for given manga id
        """
        url_endpoint = 'manga/{}'.format(manga_id)
        field = ",".join(fields)

        parameters = {'fields': field}
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)

    def manga_ranking(self, ranking_type: str, limit: int = 10, offset: int = 0, fields: list = ('name', 'id')):
        """
        function for get manga ranking api
        :param ranking_type:type of ranking
        :param limit:number of results user want default = 10
        :param offset: from where result should start from default = 0
        :param fields: fields which user want to get
        :return:details of manga sorted by ranking
        """
        url_endpoint = 'manga/ranking'
        field = ",".join(fields)

        parameters = {'ranking_type': ranking_type,
                      'limit': limit,
                      'offset': offset,
                      'fields': field}
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)
