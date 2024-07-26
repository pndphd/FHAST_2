try:
    from ..requests import get
except:
    from requests import get

from .default import DEFAULT_URL

class QmsNews(object):
    def __init__(self, i18n_texts):
        self.i18n_texts = i18n_texts

    def get_text(self, lang):
        return self.i18n_texts.get(lang, self.i18n_texts.get('en'))


class ApiClient(object):
    VERSION = 0

    request_timeout = (5, 20) # connect and read timeouts

    def __init__(self, endpoint_url=DEFAULT_URL):
        self.endpoint_url = endpoint_url
        self.__proxy = {}
        
    def set_proxy(self, proxy_host, proxy_port, proxy_user, proxy_password):
        if proxy_host != "":
            proxy_url = proxy_host
            if proxy_port != "":
                proxy_url = "%s:%s" % (proxy_url, proxy_port)
            if proxy_user != "":
                proxy_url = "%s:%s@%s" % (
                    proxy_user,
                    proxy_password,
                    proxy_url
                )

            self.__proxy = {
                "http": proxy_url,
                "https": proxy_url
            }

    @property
    def base_url(self):
        return '%s/api/v%s/' % (self.endpoint_url, self.VERSION)

    def full_url(self, sub_url):
        return self.base_url + sub_url

    def _get_json(self, url, params=None):
        _params = {}
        if params is not None:
            _params.update(params)

        response = get(url, params=_params, proxies=self.__proxy, verify=True, timeout=self.request_timeout)
        return response.json()

    def _get_content(self, url, params=None):
        response = get(url, params=params, stream=True, verify=True, timeout=self.request_timeout)
        return response.content

    def get_news(self):
        url = '%s/static/news.json' % (self.endpoint_url, )

        try:
            response = get(url, verify=True, timeout=self.request_timeout)
            if response.ok:
                news_json = response.json()
                i18n_texts = {}
                i18n_texts['en'] = news_json.get('text_en')
                i18n_texts['ru'] = news_json.get('text_ru')
                return QmsNews(i18n_texts)

        except Exception as e:
            pass

        return None
