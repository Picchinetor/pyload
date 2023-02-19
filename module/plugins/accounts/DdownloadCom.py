# -*- coding: utf-8 -*-

from ..internal.misc import search_pattern
from ..internal.XFSAccount import XFSAccount


class DdownloadCom(XFSAccount):
    __name__ = "DdownloadCom"
    __type__ = "account"
    __version__ = "0.05"
    __status__ = "testing"

    __description__ = """Ddownload.com account plugin"""
    __license__ = "GPLv3"
    __authors__ = [("GammaC0de", "nitzo2001[AT]yahoo[DOT]com")]

    PLUGIN_DOMAIN = "ddownload.com"

    PREMIUM_PATTERN = r'remium Account \(expires'
    TRAFFIC_LEFT_PATTERN = r'<span>Traffic available</span>\s*<div class="price">(?:<sup>(?P<U>[^<>]+)</sup>)?(?P<S>-?\d+|[Uu]nlimited)</div>'
    VALID_UNTIL_PATTERN = r'Premium Account \(expires ([^)]+)\)'

    @XFSAccount.logged.getter
    def logged(self):
        if super(DdownloadCom, self).logged is False:
            return False

        self.data = self.load(self.PLUGIN_URL)
        return search_pattern(self.LOGIN_SKIP_PATTERN, self.data) is not None
