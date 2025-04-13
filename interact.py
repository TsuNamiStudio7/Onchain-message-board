from utils import w3, compile_contract
from config import WALLET_ADDRESS, PRIVATE_KEY, CHAIN_ID, GAS, GAS_PRICE_GWEI

CONTRACT_ADDRESS = "0xYourDeployedContract"

abi, _ = compile_contract("MessageBoard.sol", "MessageBoard")
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

def post_message(text):
    nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)
    tx = contract.functions.postMessage(text).build_transaction({
        'from': WALLET_ADDRESS,
        'nonce': nonce,
        'chainId': CHAIN_ID,
        'gas': GAS,
        'gasPrice': w3.to_wei(GAS_PRICE_GWEI, 'gwei'),
    })
    signed = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print("✉️ Sent:", tx_hash.hex())
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("✅ Confirmed in block:", receipt.blockNumber)

def list_messages():
    count = contract.functions.getMessageCount().call()
    print(f"🧾 Total messages: {count}")
    for i in range(count):
        sender, text, timestamp = contract.functions.getMessage(i).call()
        print(f"{i+1}. {sender[:10]}: {text} ({timestamp})")

# Example
if __name__ == "__main__":
    action = input("Type 'post' to send message or 'list' to read: ")
    if action == "post":
        txt = input("Message to post: ")
        post_message(txt)
    elif action == "list":
        list_messages()
