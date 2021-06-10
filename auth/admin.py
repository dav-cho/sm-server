from django.contrib import admin
from rest_framework_simplejwt.token_blacklist.admin import (
    OutstandingTokenAdmin,
    # BlacklistedTokenAdmin,
)
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    # BlacklistedToken,
)


class OutstandingTokenAdmin(OutstandingTokenAdmin):
    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.unregister(OutstandingToken)
admin.site.register(OutstandingToken, OutstandingTokenAdmin)


# class BlacklistTokenAdmin(BlacklistedTokenAdmin):
#     def has_delete_permission(self, *args, **kwargs):
#         return True


# admin.site.unregister(BlacklistedToken)
# admin.site.register(BlacklistedToken, BlacklistTokenAdmin)
