from typing import Optional

import requests

from icon_governance.config import settings
from icon_governance.log import logger


def get_max_addresses(is_contract: bool = None) -> Optional[int]:

    endpoint = settings.COMMUNITY_API_ENDPOINT + f"/api/v1/addresses"
    if is_contract:
        endpoint += "/contracts"

    r = requests.head(endpoint)
    if r.status_code == 200:
        headers = dict(r.headers)
        if "x-total-count" in headers:
            total_records = int(headers["x-total-count"])
        elif "X-Total-Count" in headers:
            total_records = int(headers["X-Total-Count"])
        else:
            raise Exception(f"No count in headers headers: {headers}")
        return total_records
    else:
        logger.info(f"Could not head addresses")
        return None


def get_addresses(
    max_addresses: int,
    data: list = None,
    skip: int = None,
    limit: int = 100,
    is_contract: bool = None,
) -> list[dict]:
    if data is None:
        data = []
    if skip is None:
        skip = 0
    if skip >= max_addresses:
        return data

    endpoint = settings.COMMUNITY_API_ENDPOINT + f"/api/v1/addresses?skip={skip}&limit={limit}"
    if is_contract is not None:
        endpoint += "&is_contract=true"

    r = requests.get(endpoint, timeout=5)
    if r.status_code == 200:
        data += r.json()
        return get_addresses(max_addresses, data, skip + limit, is_contract=is_contract)

    return data


def get_transactions(
    from_: str = None,
    to_: str = None,
    method: str = None,
    data: list = None,
    skip: int = None,
    limit: int = 100,
) -> list[dict]:
    if data is None:
        data = []
    if skip is None:
        skip = 0

    endpoint = settings.COMMUNITY_API_ENDPOINT + f"/api/v1/transactions"
    endpoint += f"?skip={skip}&limit={limit}"

    if from_ is not None:
        endpoint += f"&from={from_}"
    if to_ is not None:
        endpoint += f"&to={to_}"
    if method is not None:
        endpoint += f"&method={method}"

    r = requests.get(endpoint)
    if r.status_code == 200:
        data += r.json()
        return get_transactions(from_=from_, to_=to_, method=method, data=data, skip=skip + limit)

    return data
