masset_events = {
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
    "DeficitMinted": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amt",
                "type": "uint256",
            }
        ],
        "name": "DeficitMinted",
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
        ],
        "name": "FeesChanged",
        "type": "event",
    },
    "ForgeValidatorChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "forgeValidator",
                "type": "address",
            }
        ],
        "name": "ForgeValidatorChanged",
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
                "name": "mAssetQuantity",
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
                "name": "mAssetQuantity",
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
    "SurplusBurned": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "creditor",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amt",
                "type": "uint256",
            },
        ],
        "name": "SurplusBurned",
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
                "name": "scaledFee",
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
