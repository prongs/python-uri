import re


class URI_DEFAULTS(object):
    """Cosntants which determine which defaults to set"""
    NONE = 0x0
    SCHEME = 0X1
    PORT = 0X02
    ALL = 0X3


def parse_query(query):
    


class URI(object):
    """docstring for URI"""
    URI_REGEX = r'(([A-Za-z][A-Za-z0-9+-.]*)://)?((\w+):(\w+)@)?(([A-Za-z0-9_.]+)(:(\d+))?)(/([A-Za-z0-9_./]*))?(\?([A-Za-z0-9_=;%.]*))?(#([A-Za-z0-9_=;%.,/]*))?'

    def __init__(self, uri, defaults=URI_DEFAULTS.NONE):
        super(URI, self).__init__()
        self.uri = uri
        self.volatile = False
        m = re.match(self.URI_REGEX, self.uri)
        self.scheme = m.group(2) or "http"
        self.username = m.group(4)
        self.password = m.group(5)
        self.authority = m.group(6)
        self.domain = m.group(7)
        self.port = m.group(9) or "80"
        self.path = m.group(11)
        self.query_string = m.group(13)
        self.fragment = m.group(15)

        self.query_dict = parse_query(self.query_string)

    def set_defaults(self, mask):
        if mask & URI_DEFAULTS.SCHEME:
            self.scheme = self.scheme or "http"
        if mask & URI_DEFAULTS.PORT:
            self.port = self.port or "80"

    def __repr__(self):
        return ", ".join([self.scheme or "None", self.username or "None", self.password or "None",
            self.authority or "None", self.domain or "None", self.port or "None", self.path or "None",
            self.query_string or "None"])


if __name__ == '__main__':
    uris = ["google.com", "http://google.com", "https://www.google.com", "ftp://rajat:pwd@iitd.com/", "http://agni.iitd.ac.in:8080/wperf/map/traceroute/youtube.com",
        "http://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0CCwQFjAB&url=http%3A%2F%2Fdocs.python.org%2Fhowto%2Fregex.html&ei=Hc6oUNebApHqrQeU8ID4BA&usg=AFQjCNGK0hq_pm4F8SR2kFxz7iayOdmtEw&sig2=IkQnRlWnfAEZbhv64z0Org",
        "https://www.interviewstreet.com/challenges/dashboard/#problems"
        ]
    for uri in uris:
        print "\t", uri
        u = URI(uri)
        print u
