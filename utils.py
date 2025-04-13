from web3 import Web3
from config import INFURA_URL

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def compile_contract(sol_file, contract_name):
    from solcx import compile_source, install_solc
    install_solc("0.8.0")
    with open(sol_file, 'r') as f:
        source = f.read()
    compiled = compile_source(source, output_values=["abi", "bin"])
    contract = compiled[f"<stdin>:{contract_name}"]
    return contract['abi'], contract['bin']
