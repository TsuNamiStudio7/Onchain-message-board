from utils import w3, compile_contract
from config import WALLET_ADDRESS, PRIVATE_KEY, CHAIN_ID, GAS, GAS_PRICE_GWEI

abi, bytecode = compile_contract("MessageBoard.sol", "MessageBoard")
MessageBoard = w3.eth.contract(abi=abi, bytecode=bytecode)

nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)
tx = MessageBoard.constructor().build_transaction({
    'from': WALLET_ADDRESS,
    'nonce': nonce,
    'chainId': CHAIN_ID,
    'gas': GAS,
    'gasPrice': w3.to_wei(GAS_PRICE_GWEI, 'gwei'),
})

signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print("🚀 Deployment TX:", tx_hash.hex())

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("✅ Contract deployed at:", tx_receipt.contractAddress)
