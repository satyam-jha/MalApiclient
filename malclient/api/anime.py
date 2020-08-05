
from .constant import *
from malclient.client import Auth


class AnimeApi(Auth):
    """
    class for all apis related to anime
    """

    def search_anime(self, anime_name: str, limit: int = 20, offset: int = 0) -> dict:
        """
        function for get anime list api

        :param anime_name: query string
        :param limit: number of results user want default = 20
        :param offset: from where result should start from default = 0
        :return: search result for your query
        """

        url_endpoint = 'anime'
        parameters = {'q': anime_name,
                      'limit': limit,
                      'offset': offset
                      }
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)

    def get_anime_details(self, anime_id: int, fields: list = ("id", "tittle", "main_picture")) -> dict:
        """
        function for get anime details api
        :param anime_id:id of anime
        :param fields: fields which user want to get
        :return:details of anime for given anime id
        """
        url_endpoint = 'anime/{}'.format(anime_id)
        field = ",".join(fields)

        parameters = {'fields': field}
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)

    def anime_ranking(self, ranking_type: str, limit: int = 10, offset: int = 0, fields: list = ("id", "tittle", "main_picture")) -> dict:
        """
        function for get anime ranking api
        :param ranking_type:type of ranking
        :param limit:number of results user want default = 10
        :param offset: from where result should start from default = 0
        :param fields: fields which user want to get
        :return:details of anime sorted by ranking
        """
        url_endpoint = 'anime/ranking'

        field = ",".join(fields)

        parameters = {'ranking_type': ranking_type,
                      'limit': limit,
                      'offset': offset,
                      'fields': field}

        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)

    def seasonal_anime(self, year: int, season: str, sort: str = 'anime_num_list_users', limit: int = 10,
                       offset: int = 0, fields: list = ("id", "tittle", "main_picture")) -> dict:
        """
        function for get seasonal anime api
        :param year:for which year user want to get seasonal anime
        :param season: for which season user want to get anime
        :param sort: specify result should be sorted by score or number of users
        :param limit:number of results user want default = 10
        :param offset: from where result should start from default = 0
        :param fields: fields which user want to get
        :return: details of seasonal anime
        """
        url_endpoint = 'anime/season/{}/{}'.format(year, season)
        field = ",".join(fields)

        parameters = {'sort': sort,
                      'limit': limit,
                      'offset': offset,
                      'fields': field}

        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)

    def suggested_anime(self, limit: int = 10, offset: int = 0, fields: list = ("id", "tittle", "main_picture")) -> dict:
        """
        function to get suggested anime api
        :param limit:number of results user want default = 10
        :param offset: from where result should start from default = 0
        :param fields: fields which user want to get
        :return:Returns suggested anime for the authorized user
        """
        url_endpoint = 'anime/suggestions'
        field = ",".join(fields)

        parameters = {'limit': limit,
                      'offset': offset,
                      'fields': field}

        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)
