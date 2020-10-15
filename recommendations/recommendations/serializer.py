from typing import List


class BaseDictSerializer:
    fields: List[str] = []

    def serialize(self, entry):
        return {field: entry[field] for field in self.fields}

    def serialize_many(self, entrys):
        return [self.serialize(entry) for entry in entrys]


class ProductDictSerializer(BaseDictSerializer):
    fields = ["sku", "title", "description", "price"]
