feeder_pool_events = {
    "Approval": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "spender",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "type": "event",
    },
    "BassetsMigrated": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address[]",
                "name": "bAssets",
                "type": "address[]",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "newIntegrator",
                "type": "address",
            },
        ],
        "name": "BassetsMigrated",
        "type": "event",
    },
    "CacheSizeChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "cacheSize",
                "type": "uint256",
            }
        ],
        "name": "CacheSizeChanged",
        "type": "event",
    },
    "FeesChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "swapFee",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "redemptionFee",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "govFee",
                "type": "uint256",
            },
        ],
        "name": "FeesChanged",
        "type": "event",
    },
    "Minted": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "minter",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "recipient",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "output",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "input",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "inputQuantity",
                "type": "uint256",
            },
        ],
        "name": "Minted",
        "type": "event",
    },
    "MintedMulti": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "minter",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "recipient",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "output",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address[]",
                "name": "inputs",
                "type": "address[]",
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "inputQuantities",
                "type": "uint256[]",
            },
        ],
        "name": "MintedMulti",
        "type": "event",
    },
    "Paused": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address",
            }
        ],
        "name": "Paused",
        "type": "event",
    },
    "Redeemed": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "redeemer",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "recipient",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "mAssetQuantity",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "output",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "outputQuantity",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "scaledFee",
                "type": "uint256",
            },
        ],
        "name": "Redeemed",
        "type": "event",
    },
    "RedeemedMulti": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "redeemer",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "recipient",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "mAssetQuantity",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address[]",
                "name": "outputs",
                "type": "address[]",
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "outputQuantity",
                "type": "uint256[]",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "scaledFee",
                "type": "uint256",
            },
        ],
        "name": "RedeemedMulti",
        "type": "event",
    },
    "StartRampA": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "currentA",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "targetA",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "startTime",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "rampEndTime",
                "type": "uint256",
            },
        ],
        "name": "StartRampA",
        "type": "event",
    },
    "StopRampA": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "currentA",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "time",
                "type": "uint256",
            },
        ],
        "name": "StopRampA",
        "type": "event",
    },
    "Swapped": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "swapper",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "input",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "output",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "outputAmount",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "fee",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "recipient",
                "type": "address",
            },
        ],
        "name": "Swapped",
        "type": "event",
    },
    "Transfer": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "type": "event",
    },
    "Unpaused": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address",
            }
        ],
        "name": "Unpaused",
        "type": "event",
    },
    "WeightLimitsChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint128",
                "name": "min",
                "type": "uint128",
            },
            {
                "indexed": False,
                "internalType": "uint128",
                "name": "max",
                "type": "uint128",
            },
        ],
        "name": "WeightLimitsChanged",
        "type": "event",
    },
}
