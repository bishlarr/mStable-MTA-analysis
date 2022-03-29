import asyncio
from typing import Any
import os

from datetime import datetime
import numpy as np

import pandas as pd
from ctc import evm, rpc

from abis import staked_token_mta, staked_token_bpt, emissions_controller_logic
import utils.contracts as mc
from ctc.protocols import uniswap_v2_utils, uniswap_v3_utils, sushi_utils, balancer_utils
from ctc.protocols import chainlink_utils

async def store_blocks_timestamps(dates: list[int], path: str):
    """
    Get timestamps of the given blocks, then link each block to its date (day here)
    """
    timestamps = (dates.astype(np.int64) // 10 ** 9).to_list()
    data: list = await evm.async_get_blocks_of_timestamps(
        timestamps 
    )
    df = pd.DataFrame({'date':dates, 'timestamp':timestamps ,'block_number':data})
    block_range = range(df.block_number.min(), df.block_number.max() + 6000) # 6000 blocks almost eq to a day
    df = pd.merge(pd.DataFrame({'block_number':block_range}), df.loc[:, ['date', 'block_number']],
                  how='left', on='block_number')
    df.ffill(inplace=True)
    df.to_parquet(path)

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
    
async def store_dex_swaps(pool: str, path: str, module: Any):
    """
    Get all swaps from a pool of a specific dex
    """
    df: pd.DataFrame = await module.async_get_pool_swaps(pool)
    df.to_parquet(path)
    
async def store_prices(address: str, path: str):
    
    df: pd.DataFrame = await chainlink_utils.async_get_feed_data(address)
    df.to_parquet(path)


async def main():
    
    ### Timestamps ###
    await store_blocks_timestamps(
        pd.date_range(start="2020-01-01",end=datetime.today()),
        "./mStable-data/data/block_to_timestamp.parquet"
    )
    
    ### MTA ###
    
    await store_transfer(mc.MTA, "./mStable-data/data/mta_transfer.parquet")
    
    ### MBPT ###
    
    await store_transfer(mc.mBPT, "./mStable-data/data/mbpt_transfer.parquet")
    
    ### StkMTA ###

    await store_event_abi(
        mc.stkMTA,
        staked_token_mta.staked_token_mta_events["Staked"],
        "./mStable-data/data/stkmta_staked.parquet",
    )
    
    await store_event_abi(
        mc.stkMTA,
        staked_token_mta.staked_token_mta_events["Withdraw"],
        "./mStable-data/data/stkmta_withdraw.parquet",
    )
    
    ### StkBPT ###
    
    await store_event_abi(
        mc.stkBPT,
        staked_token_bpt.staked_token_bpt_events["Staked"],
        "./mStable-data/data/stkbpt_staked.parquet",
    )
    
    await store_event_abi(
        mc.stkBPT,
        staked_token_bpt.staked_token_bpt_events["Withdraw"],
        "./mStable-data/data/stkbpt_withdraw.parquet",
    )
    
    await store_event_abi(
        mc.mStable_emissions_controller,
        emissions_controller_logic.emissions_controller_logic_events["DistributedReward"],
        "./mStable-data/data/emissions_controller_dist_rewards.parquet",
    )
    
    await store_event_abi(
        mc.mStable_emissions_controller,
        emissions_controller_logic.emissions_controller_logic_events["AddedDial"],
        "./mStable-data/data/emissions_controller_added_dial.parquet",
    )
    
    """
    ### Bugs with ctc lib (unable to get ABI from etherscan)
    
    ### DEXes TRADES ###
    await store_dex_swaps(
        "0xD0effc6828972483db1c64106f71d6AD12606a53", 
        "./mStable-data/data/test.parquet", 
        uniswap_v3_utils
    )
    
    
    ### ORACLE PRICES ###
    await store_prices(
        mc.MTA,
        "./mStable-data/data/mta_prices.parquet"
    )
    """
    
    await rpc.async_close_http_session()
    
if __name__ == "__main__":
    asyncio.run(main())    
    
