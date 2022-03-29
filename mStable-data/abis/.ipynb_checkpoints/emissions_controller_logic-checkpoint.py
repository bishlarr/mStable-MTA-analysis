emissions_controller_logic_events = {
    "AddStakingContract": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "stakingContract",
                "type": "address",
            }
        ],
        "name": "AddStakingContract",
        "type": "event",
    },
    "AddedDial": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "dialId",
                "type": "uint256",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "recipient",
                "type": "address",
            },
        ],
        "name": "AddedDial",
        "type": "event",
    },
    "DistributedReward": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "dialId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "DistributedReward",
        "type": "event",
    },
    "DonatedRewards": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "dialId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "DonatedRewards",
        "type": "event",
    },
    "PeriodRewards": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]",
            }
        ],
        "name": "PeriodRewards",
        "type": "event",
    },
    "PreferencesChanged": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "voter",
                "type": "address",
            },
            {
                "components": [
                    {"internalType": "uint256", "name": "dialId", "type": "uint256"},
                    {"internalType": "uint256", "name": "weight", "type": "uint256"},
                ],
                "indexed": False,
                "internalType": "struct Preference[]",
                "name": "preferences",
                "type": "tuple[]",
            },
        ],
        "name": "PreferencesChanged",
        "type": "event",
    },
    "SourcesPoked": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "voter",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newVotesCast",
                "type": "uint256",
            },
        ],
        "name": "SourcesPoked",
        "type": "event",
    },
    "UpdatedDial": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "dialId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "disabled",
                "type": "bool",
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "_notify",
                "type": "bool",
            },
        ],
        "name": "UpdatedDial",
        "type": "event",
    },
    "VotesCast": {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "stakingContract",
                "type": "address",
            },
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
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "VotesCast",
        "type": "event",
    },
}
