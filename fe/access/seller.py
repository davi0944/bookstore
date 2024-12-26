import requests
from urllib.parse import urljoin
from fe.access import book
from fe.access.auth import Auth


class Seller:
    def __init__(self, url_prefix, seller_id: str, password: str):
        self.url_prefix = urljoin(url_prefix, "seller/")
        self.seller_id = seller_id
        self.password = password
        self.terminal = "my terminal"
        self.auth = Auth(url_prefix)
        self.token = self._login()

    def _login(self) -> str:
        code, token = self.auth.login(self.seller_id, self.password, self.terminal)
        assert code == 200
        return token

    def _send_request(self, endpoint: str, payload: dict) -> int:
        url = urljoin(self.url_prefix, endpoint)
        headers = {"token": self.token}
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code

    def create_store(self, store_id: str) -> int:
        payload = {
            "user_id": self.seller_id,
            "store_id": store_id,
        }
        return self._send_request("create_store", payload)

    def add_book(self, store_id: str, stock_level: int, book_info: book.Book) -> int:
        payload = {
            "user_id": self.seller_id,
            "store_id": store_id,
            "book_info": book_info.__dict__,
            "stock_level": stock_level,
        }
        return self._send_request("add_book", payload)

    def add_stock_level(self, seller_id: str, store_id: str, book_id: str, add_stock_num: int) -> int:
        payload = {
            "user_id": seller_id,
            "store_id": store_id,
            "book_id": book_id,
            "add_stock_level": add_stock_num,
        }
        return self._send_request("add_stock_level", payload)

    def deliver_book(self, seller_id: str, order_id: str) -> int:
        payload = {
            "user_id": seller_id,
            "order_id": order_id,
        }
        return self._send_request("deliver_book", payload)