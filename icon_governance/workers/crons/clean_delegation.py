from sqlmodel import delete, select

from icon_governance.log import logger
from icon_governance.models.delegations import Delegation
from icon_governance.utils.rpc import getDelegation

delegation_delete_count = 0


def clean_delegations(session):
    logger.info(f"Starting {__name__} cron")

    query = select(Delegation.address).distinct()
    result = session.execute(query)
    addresses: list[str] = result.scalars().all()

    for a in addresses:
        query = select(Delegation).where(Delegation.address == a)
        result = session.execute(query)
        delegations_db: list[Delegation] = result.scalars().all()

        delegations_rpc = getDelegation(a).json()["result"]["delegations"]
        delegations_rpc_preps = [i["address"] for i in delegations_rpc]

        for d in delegations_db:
            if d.prep_address not in delegations_rpc_preps:
                # Case where the prep is not in the delegations_rpc (source of truth)
                d.value = 0
            else:
                # Case where we have it in DB and are just fixing the value
                delegation_item = [
                    delegations_rpc.pop(i)
                    for i, v in enumerate(delegations_rpc)
                    if v["address"] == d.prep_address
                ][0]
                d.value = int(delegation_item["value"], 16)

            session.merge(d)
        for dr in delegations_rpc:
            # Case where we are missing it in DB and need to add a new delegation
            d = Delegation(
                address=a,
                prep_address=dr["address"],
                value=int(dr["value"], 16),  # noqa - condecimal type
                last_updated_block=0,
                delegator=a,
            )
            session.merge(d)
        session.commit()

    # Finally delete all the old delegations
    statement = delete(Delegation).where(Delegation.value == 0)
    session.execute(statement)
    session.commit()

    logger.info(f"Ending {__name__} cron")


if __name__ == "__main__":
    from icon_governance.db import session_factory

    with session_factory() as session:
        clean_delegations(session=session)
