from rest_framework.throttling import SimpleRateThrottle


class VisitThrottle(SimpleRateThrottle):
    rate = '5/m'
    # 频率每分钟五次 单位可以是 s（秒） m（分钟）h（小时）d（天）
    scope = 'vistor'

    def get_cache_key(self, request, view):
        return self.get_ident(request)
