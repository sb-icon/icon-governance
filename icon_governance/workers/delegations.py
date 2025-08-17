from sqlmodel import select

from icon_governance.log import logger
from icon_governance.models.delegations import Delegation
from icon_governance.utils.rpc import convert_hex_int


def set_delegation(session, data, address, block_height, hash):
    """
    Set the delegation for the voters tab on the p-rep details page. Takes in all
    setDelegation payloads and updates the records with them. First checks the db to
    see if the address has sent a Tx with a higher last_updated_block. If it is older,
    ignore the Tx. If higher, then delete all the old delegations and insert a the new
    delegations. This is for out of order processing.
    """

    params = data["params"]

    if "delegations" not in params:
        logger.info(f"Skipping because no delegation field.")
        return

    # # Select all the records
    # statement = select(Delegation).where(Delegation.address == address)
    #
    # result = session.execute(statement)
    # address_delegation = result.scalars().all()
    #
    # if len(address_delegation) != 0:
    #     last_updated_block_set = set([i.last_updated_block for i in address_delegation])
    #     if len(last_updated_block_set) > 1:
    #         logger.info(
    #             f"Found multiple different last_updated_block " f"- {last_updated_block_set}"
    #         )
    #
    #     last_updated_block = address_delegation[0].last_updated_block
    #     if last_updated_block is None:
    #         last_updated_block = 0
    #
    #     if last_updated_block > block_height:
    #         # Already have latest data in DB
    #         logger.info(
    #             f"Skipping setDelegation {hash} - before last updated block "
    #             f"- {last_updated_block_set}"
    #         )
    #         return
    #     # elif last_updated_block == block_height:
    #     #     # Already have latest data in DB
    #     #     logger.info(
    #     #         f"Skipping setDelegation {hash} - already updated this Tx"
    #     #         f"- {last_updated_block_set}"
    #     #     )
    #     #     return
    #     else:
    #         for d in address_delegation:
    #             session.delete(d)
    #             session.flush()

    for d in params["delegations"]:
        delegation = Delegation(
            address=address,
            prep_address=d["address"],
            value=int(d["value"], 0),
            last_updated_block=block_height,
            delegator=address,
        )

        session.merge(delegation)
        session.commit()
