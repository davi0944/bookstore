from fe import conf
from fe.access import seller, auth


def register_new_seller(user_id: str, password: str) -> seller.Seller:
    auth_instance = auth.Auth(conf.URL)
    registration_status = auth_instance.register(user_id, password)
    assert registration_status == 200
    seller_instance = seller.Seller(conf.URL, user_id, password)
    return seller_instance
