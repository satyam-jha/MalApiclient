from .constant import *
from malclient.client import Auth



class UserAnimelist(Auth):

    def update_my_animelist(self, anime_id: int, status: str, is_rewatching: bool, score: int,
                            num_watched_episodes: int, priority: int, num_times_rewatched: int
                            , rewatch_value: int, tags: str, comments: str) -> dict:
        """

        :param anime_id:
        :param status:
        :param is_rewatching:
        :param score:
        :param num_watched_episodes:
        :param priority:
        :param num_times_rewatched:
        :param rewatch_value:
        :param tags:
        :param comments:
        :return:
        """

        url_endpoint = 'anime/{}/my_list_status'.format(anime_id)
        parameters = {'status': status,
                      'is_rewatching': is_rewatching,
                      'score': score,
                      'num_watched_episodes': num_watched_episodes,
                      'priority': priority,
                      'num_times_rewatched': num_times_rewatched,
                      'rewatch_value': rewatch_value,
                      'tags': tags,
                      'comments': comments}
        return self.get_response(url=url_endpoint, method=patch_method, parameters=parameters)

    def remove_anime(self, anime_id: int) -> dict:
        """

        :param anime_id:
        :return:
        """

        url_endpoint = 'anime/{}/my_list_status'.format(anime_id)
        parameters = {}
        return self.get_response(url=url_endpoint, method=del_method, parameters=parameters)

    def my_animelist(self, sort: str, status=None, limit: int = 10, offset: int = 0):

        url_endpoint = 'users/@me/animelist'
        parameters = {'status': status,
                      'sort': sort,
                      'limit': limit,
                      'offset': offset}
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)


class UserMangalist(Auth):

    def update_my_mangalist(self, manga_id, status, is_rereading, score, num_volumes_read, num_chapter_read, priority, num_times_reread, reread_value, tags, comments):

        url_endpoint = 'manga/{}/my_list_status'.format(manga_id)
        parameters = {'status': status,
                      'is_rereading': is_rereading,
                      'score': score,
                      'num_volumes_read': num_volumes_read,
                      'num_chapter_read': num_chapter_read,
                      'priority': priority,
                      'num_times_reread': num_times_reread,
                      'reread_value': reread_value,
                      'tags': tags,
                      'comments': comments}
        return self.get_response(url=url_endpoint, method=patch_method, parameters=parameters)

    def remove_manga(self, manga_id):

        url_endpoint = 'manga/{}/my_list_status'.format(manga_id)
        parameters = {}
        return self.get_response(url=url_endpoint, method=del_method, parameters=parameters)

    def my_mangalist(self, sort, status=None, limit=10, offset=0):

        url_endpoint = 'users/@me/mangalist'
        parameters = {'status': status,
                      'sort': sort,
                      'limit': limit,
                      'offset': offset}
        return self.get_response(url=url_endpoint, method=get_method, parameters=parameters)
