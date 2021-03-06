[
    {
        "name": "youkuloader",
        "find": "http:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/swf\/loaders?\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/loader.swf",
        "extra": "adkillrule"
    },
    {
        "name": "youkuplayer",
        "find": "http:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/swf\/q?player.*\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/player.swf",
        "extra": "adkillrule"
    },
    {
        "name": "ku6",
        "find": "http:\/\/player\.ku6cdn\.com\/default\/.*\/(v|player)\.swf",
        "replace": "hostsite/ku6.swf",
        "extra": "adkillrule"
    },
    {
        "name": "tudou",
        "find": "http:\/\/js\.tudouui\.com\/.*PortalPlayer[^\.]*\.swf",
        "exfind": "narutom",
        "replace": "hostsite/tudou.swf",
        "css": ".player {height: inherit !important;}",
        "extra": "adkillrule"
    },
    {
        "name": "tudou_olc",
        "find": "http:\/\/js\.tudouui\.com\/.*olc[^\.]*\.swf",
        "replace": "hostsite/olc_8.swf",
        "extra": "adkillrule"
    },
    {
        "name": "tudou_sp",
        "find": "http:\/\/js\.tudouui\.com\/.*SocialPlayer[^\.]*\.swf",
        "replace": "hostsite/sp.swf",
        "extra": "adkillrule"
    },
    {
        "name": "letv",
        "find": "http:\/\/.*letv[\w]*\.com\/.*\/((?!(Live|seed|Disk))(S[\w]{2,3})?(?!Live)[\w]{4}|swf)Player*\.swf",
        "exfind": "(bili|acfun|com\/zt|duowan)",
        "replace": "hostsite/letv.swf",
        "extra": "adkillrule"
    },
    {
        "name": "letvpccs",
        "find": "http:\/\/www.letv.com\/.*\/playerapi\/pccs_(?!(live|sdk)).*_?(\d+)\.xml",
        "replace": "http://www.letv.com/cmsdata/playerapi/pccs_sdk_20141113.xml",
        "extra": "adkillrule"
    },
    {
        "name": "pplive",
        "find": "(\/\/|\.)player\.pplive\.cn.*\/PPLivePlugin\.swf",
        "replace": "about:blank",
        "extra": "adkillrule"
    },
    {
        "name": "iqiyi",
        "find": "https?:\/\/www\.iqiyi\.com\/(player\/(\d+\/Player|[a-z0-9]*)|common\/flashplayer\/\d+\/(Main|Share)?Player.*_(.|ad\d+))\.swf",
        "exfind": "(baidu|61|178)\.iqiyi\.com|weibo|yaku\.tv|bilibili|acfun|(music|tieba)\.baidu",
        "replace": "hostsite/iqiyi5.swf",
        "extra": "adkillrule"
    },
    {
        "name": "pps",
        "find": "https?:\/\/www\.iqiyi\.com\/common\/.*\/pps[\w]+.swf",
        "replace": "hostsite/iqiyi_out.swf",
        "extra": "adkillrule"
    },
    {
        "name": "sohu",
        "find": "http:\/\/tv\.sohu\.com\/upload\/swf\/(?!(live|\d+|ap)).*\d+\/(main|PlayerShell)\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/sohu.swf",
        "extra": "adkillrule"
    },
    {
        "name": "sohu_live",
        "find": "http:\/\/(tv\.sohu\.com\/upload\/swf\/(live\/|)\d+|61\.135\.176\.223.*\/.*)\/(main|PlayerShell)\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/sohu_live.swf",
        "extra": "adkillrule"
    },
    {
        "name": "duowan",
        "find": "http:\/\/untitled\.dwstatic\.com\/.*",
        "replace": "about:blank",
        "extra": "adkillrule"
    }
]
