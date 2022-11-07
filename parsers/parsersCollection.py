from parsers.brandshopRu import BrandshopParse
from parsers.dnsshopRu import DnsShopParse
from parsers.lamodaRu import LamodaParse
from parsers.mvideoRu import MvideoParse


class ParsersCollection:
    def GetParser(domain: str):
        match domain:
            case "dns-shop.ru":
                return DnsShopParse()
            case "brandshop.ru":
                return BrandshopParse()
            case "lamoda.ru":
                return LamodaParse()
            case "mvideo.ru":
                return MvideoParse()
