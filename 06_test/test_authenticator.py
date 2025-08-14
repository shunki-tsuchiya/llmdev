import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth

def test_register_success(authenticator):
    authenticator.register("user1", "pass123")
    assert "user1" in authenticator.users
    assert authenticator.users["user1"] == "pass123"

def test_register_existing_user(authenticator):
    authenticator.register("user2", "pass123")
    with pytest.raises(ValueError) as e:
        authenticator.register("user2", "pass456")
    assert "エラー: ユーザーは既に存在します。" in str(e.value)

def test_login_success(authenticator):
    authenticator.register("user3", "pass123")
    result = authenticator.login("user3", "pass123")
    assert result == "ログイン成功"

def test_login_worng_password(authenticator):
    authenticator.register("user4", "pass123")
    with pytest.raises(ValueError) as e:
        authenticator.login("user4", "worngpass")
    assert "エラー: ユーザー名またはパスワードが正しくありません。" in str(e.value)
