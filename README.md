# MTA Analysis

Please create a python notebook, do an on-chain analysis of our MTA token, and give us your findings.

## Running

```bash
# Create a virtualenv
virtualenv venv
source venv/bin/activate
# Install the requirements
pip install -r requirements.txt
# Config ctc
ctc setup
# Get data
python mStable-data/data.py
# Transform ABI into a Python file
python mStable-data/utils/abi_to_py.py
# Run jupyter
jupyter-lab
```

## Things to help you

### Getting on-chain data

There is an example of getting on-chain in the [data.py](./mStable-data/data.py).

The example uses the FEI team's library called [checkthechain](https://github.com/fei-protocol/checkthechain).
Create an account on [alchemyapi.io,](http://alchemyapi.io/) [infura.io](http://infura.io/), get a mainnet node and set the URL for the library to use.

```bash
export NODE_URL=https://eth-mainnet.alchemyapi.io/v2/...
```

### Contract addresses & ABIs

There is already [a file](./mStable-data/utils/contracts.py) with some of the addresses from mStable and [abis](./mStable-data/abis/)

If you need to find more information, you can find it on [https://developers.mstable.org/](https://developers.mstable.org/)

**ABIs**: If you want to use another ABI that is not in the project, drop it in the [abis folder](./mStable-data/abis/) and modify [abi_to_py.py](./mStable-data/utils/abi_to_py.py) to generate the python file.

### Off-chain

Feel free to use other off-chain services to get more data to help with your insights
