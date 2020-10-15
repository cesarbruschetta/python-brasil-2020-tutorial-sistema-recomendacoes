import json
from aiohttp.web import Response
from typing import Any, Dict, Optional

from .dao_mongo import MongoDB
from .serializer import ProductDictSerializer

CONTENT_TYPE = "application/json"


class Controller:
    def __init__(self, *args, **kwargs):
        self.db = MongoDB()
        self.product_serializer = ProductDictSerializer()
        super().__init__(*args, **kwargs)

    def _get_bad_request(self, message: str) -> Response:
        return self._get_response(400, {"message": message})

    def _get_response(
        self,
        status: int,
        body: Any = None,
        cast: bool = True,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        if cast and body is not None:
            body = json.dumps(body)

        if headers is None:
            headers = {}

        headers.update(
            {
                "access-control-allow-origin": "*",
                "access-control-expose-headers": "*",
                "access-control-allow-headers": "*",
                "access-control-allow-methods": "*",
            }
        )

        return Response(
            status=status,
            body=body,
            content_type=CONTENT_TYPE,
            headers=headers,
        )

    def healthcheck(self) -> Response:
        return self._get_response(200)

    def get_options(self, id: Optional[int] = None) -> Response:
        return self._get_response(200)

    async def get_recommendations(self) -> Response:
        product = self.db.products().find_one()
        products = [product]
        return self._get_response(200, self.product_serializer.serialize_many(products))

    async def get_recommendations_products(self, product_sku: str) -> Response:
        product = self.db.products().find_one({"sku": product_sku})
        products = [product]
        return self._get_response(200, self.product_serializer.serialize_many(products))


c = Controller()
