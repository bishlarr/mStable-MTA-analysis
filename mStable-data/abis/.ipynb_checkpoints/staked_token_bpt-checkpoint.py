staked_token_bpt_events = {
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
    "BalClaimed": {
        "anonymous": False,
        "inputs": [],
        "name": "BalClaimed",
        "type": "event",
    },
    "BalRecipientChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "newRecipient",
                "type": "address",
            }
        ],
        "name": "BalRecipientChanged",
        "type": "event",
    },
    "Cooldown": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "percentage",
                "type": "uint256",
            },
        ],
        "name": "Cooldown",
        "type": "event",
    },
    "CooldownExited": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            }
        ],
        "name": "CooldownExited",
        "type": "event",
    },
    "DelegateChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "delegator",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "fromDelegate",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "toDelegate",
                "type": "address",
            },
        ],
        "name": "DelegateChanged",
        "type": "event",
    },
    "DelegateVotesChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "delegate",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "previousBalance",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newBalance",
                "type": "uint256",
            },
        ],
        "name": "DelegateVotesChanged",
        "type": "event",
    },
    "FeesConverted": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "bpt",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "mta",
                "type": "uint256",
            },
        ],
        "name": "FeesConverted",
        "type": "event",
    },
    "GovernanceHookChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "hook",
                "type": "address",
            }
        ],
        "name": "GovernanceHookChanged",
        "type": "event",
    },
    "KeeperUpdated": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "newKeeper",
                "type": "address",
            }
        ],
        "name": "KeeperUpdated",
        "type": "event",
    },
    "PriceCoefficientUpdated": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newPriceCoeff",
                "type": "uint256",
            }
        ],
        "name": "PriceCoefficientUpdated",
        "type": "event",
    },
    "Recollateralised": {
        "anonymous": False,
        "inputs": [],
        "name": "Recollateralised",
        "type": "event",
    },
    "RewardAdded": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "reward",
                "type": "uint256",
            }
        ],
        "name": "RewardAdded",
        "type": "event",
    },
    "RewardPaid": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
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
                "name": "reward",
                "type": "uint256",
            },
        ],
        "name": "RewardPaid",
        "type": "event",
    },
    "SlashRateChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newRate",
                "type": "uint256",
            }
        ],
        "name": "SlashRateChanged",
        "type": "event",
    },
    "Staked": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "delegatee",
                "type": "address",
            },
        ],
        "name": "Staked",
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
    "Withdraw": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
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
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "Withdraw",
        "type": "event",
    },
    "WrapperBlacklisted": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "wallet",
                "type": "address",
            }
        ],
        "name": "WrapperBlacklisted",
        "type": "event",
    },
    "WrapperWhitelisted": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "wallet",
                "type": "address",
            }
        ],
        "name": "WrapperWhitelisted",
        "type": "event",
    },
}
