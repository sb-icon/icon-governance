import asyncio

from loguru import logger

from icon_governance.metrics import prom_metrics
from icon_governance.models.delegations import Delegation
from icon_governance.utils.api import get_addresses, get_max_addresses
from icon_governance.utils.async_rpc import get_delegation


def run_address_stake(session):
    """
    This cron gets the stake for a set of addresses, either contracts or normal eoa.
     It works by getting the max_addresses for either and iterating over those addr
     to get their delegation. It then inserts the delegation into the DB which is
     always another eoa since the contract delegates for these addresses.
    """
    logger.info(f"Starting {__name__} cron")

    max_addresses = get_max_addresses(is_contract=True)
    batch_size = 10  # number of `limits` to run
    limit = 100

    for i in range(0, int(max_addresses / (batch_size * limit)) + 1):
        address_index = i * (batch_size * limit)
        logger.info(f"Running address index={address_index} out of {max_addresses}")
        addresses = get_addresses(
            max_addresses=address_index + batch_size * limit,
            skip=address_index,
            is_contract=True,
        )

        delegations = asyncio.run(
            get_delegation(
                addresses=addresses,
            )
        )

        for i, d in enumerate(delegations):
            if d["totalDelegated"] == "0x0":
                continue
            for delegation in d["delegations"]:
                try:
                    delegation_db = Delegation(
                        address=addresses[i]["address"],
                        prep_address=delegation["address"],
                        value=int(delegation["value"], 16),
                        delegator="",
                    )
                    if addresses[i]["address"].startswith("hx"):
                        print()

                    session.merge(delegation_db)
                except IndexError:
                    logger.info(f"error indexing delegation for {d} in {addresses[i]}")
            session.commit()

    prom_metrics.preps_attributes_cron_ran.inc()
    logger.info(f"Ending {__name__} cron")


if __name__ == "__main__":
    from icon_governance.db import session_factory

    with session_factory() as session:
        run_address_stake(session=session)
