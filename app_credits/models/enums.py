from enum import Enum


class CategoryNames(str, Enum):
        ISSUANCE_EN = "issuance"
        ISSUANCE_UA = "видача"

        COLLECTION_EN = "collection"
        COLLECTION_UA = "збір"
        PERCENT_EN = "percent"
        PERCENT_UA = "відсотки"
        BODY_UA = "тіло"
        BODY_EN = "body"
