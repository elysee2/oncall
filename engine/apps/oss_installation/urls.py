from django.urls import include, path

from common.api_helpers.optional_slash_router import OptionalSlashRouter, optional_slash_path

from .views import CloudConnectionView, CloudUsersView, CloudUserView

router = OptionalSlashRouter()
router.register("cloud_users", CloudUserView, basename="cloud-users")

urlpatterns = [
    path("", include(router.urls)),
    optional_slash_path("cloud_users", CloudUsersView.as_view(), name="cloud-users-list"),
    optional_slash_path("cloud_connection", CloudConnectionView.as_view(), name="cloud-connection-status"),
]
