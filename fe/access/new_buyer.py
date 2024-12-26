from fe import conf
from fe.access import buyer, auth


def register_new_buyer(user_id: str, password: str) -> buyer.Buyer:
    auth_instance = auth.Auth(conf.URL)
    registration_status = auth_instance.register(user_id, password)
    assert registration_status == 200
    buyer_instance = buyer.Buyer(conf.URL, user_id, password)
    return buyer_instance
