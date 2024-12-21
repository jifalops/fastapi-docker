import pytest

from app.app import App
from app.auth.service_memory import AuthServiceMock
from app.subscription.service_mock import SubscriptionServiceMock
from app.subscription_portal.service_stripe import SubscriptionPortalServiceStripe
from app.user.repo_in_mem import UserRepoInMem
from app.user.service import UserService


@pytest.fixture
def app():
    return App(
        auth=AuthServiceMock(),
        subscription=SubscriptionServiceMock(),
        subscription_portal=SubscriptionPortalServiceStripe(),
        user=UserService(repo=UserRepoInMem()),
    )


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    for item in items:
        if "_integration_test" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "_e2e_test" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)
        elif "_test.py" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
