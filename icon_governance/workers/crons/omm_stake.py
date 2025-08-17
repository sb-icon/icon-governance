import json

from loguru import logger

from icon_governance.metrics import prom_metrics
from icon_governance.models.delegations import Delegation
from icon_governance.utils.api import get_transactions
from icon_governance.utils.rpc import getDelegation, post_rpc_json


def run_omm_stake(session):
    """
    This cron parsed txs like this one:
    https://tracker.icon.community/transaction/0x46316b38e758a2bd3f2d9d26f6fbe3b30d119a534703a94d23c7ae8da76d29b4
    """
    logger.info("Starting address stake cron")

    omm_address = "cx841f29ec6ce98b527d49a275e87d427627f1afe5"
    omm_transactions = get_transactions(
        to_=omm_address,
        method="updateDelegations",
    )

    for i in omm_transactions:
        try:
            delegations = json.loads(i["data"])["params"]["_delegations"]
        except KeyError:
            continue
        for d in delegations:
            # delegation = post_rpc_json(getDelegation(address=d['_address']))
            # if delegation is None:
            #     continue
            print()
            delegation_db = Delegation(
                address=i["from_address"],
                prep_address=d["_address"],
                value=int(d["_votes_in_per"], 16),
                delegator=omm_address,
            )

            session.merge(delegation_db)
        session.commit()

    prom_metrics.preps_attributes_cron_ran.inc()
    logger.info("Ending stake cron")


if __name__ == "__main__":
    from icon_governance.db import session_factory

    with session_factory() as session:
        run_omm_stake(session=session)
