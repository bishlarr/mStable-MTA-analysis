import asyncio
from typing import Any

import pandas as pd
from ctc import evm, rpc

from abis import staked_token_mta
from utils.contracts import MTA, stkMTA


async def store_transfer(address: str, path: str):
    """
    Get all transfer events from an ERC20 token and store the DataFrame in a parquet file
    """
    df: pd.DataFrame = await evm.async_get_erc20_transfers(
        token_address=address,
        event_name="Transfer",
    )
    df.to_parquet(path)


async def store_event_abi(address: str, event_abi: dict[str, Any], path: str):
    """
    Get all events from a token of a specific ABI and store the DataFrame in a parquet file
    """
    df: pd.DataFrame = await evm.async_get_events(
        contract_address=address, event_abi=event_abi
    )
    df.to_parquet(path)


async def main():
    await store_transfer(MTA, "./mStable-data/data/mta_transfer.parquet")
    await store_event_abi(
        stkMTA,
        staked_token_mta.staked_token_mta_events["Staked"],
        "./mStable-data/data/stkmta_staked.parquet",
    ),
    await rpc.async_close_http_session()


if __name__ == "__main__":
    asyncio.run(main())
