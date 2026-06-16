import sys
import os

# Add src to pythonpath
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.blockchain.web3_client import web3_client
from src.blockchain.config import settings
from web3 import Web3

def main():
    print("--- 1. Network Information ---")
    print(f"RPC Provider: {settings.RPC_URL}")
    print(f"Contract Address: {settings.CONTRACT_ADDRESS}")
    
    if web3_client.w3 and web3_client.w3.is_connected():
        print(f"Connected: True")
        print(f"Chain ID: {web3_client.w3.eth.chain_id}")
    else:
        print("Connected: False")
        
    print("\n--- 3. Smart Contract Verification ---")
    print(f"ABI Loaded: {web3_client.contract is not None}")
    
    if web3_client.w3 and web3_client.contract:
        try:
            # check if contract has code
            code = web3_client.w3.eth.get_code(web3_client.contract.address)
            print(f"Contract Deployed at Address: {len(code) > 2}")
        except Exception as e:
            print(f"Contract Code Check Error: {e}")
    else:
        print("Contract Deployed at Address: N/A (Not connected)")

    print("\n--- 4. Runtime Configuration ---")
    print(f"OFFLINE_SIMULATION flag in settings: {settings.OFFLINE_SIMULATION}")
    print(f"web3_client.is_simulation: {web3_client.is_simulation}")
    
    if web3_client.is_simulation:
        if settings.OFFLINE_SIMULATION:
            print("Execution Context: Local Simulator (Offline Simulation configured)")
        else:
            print("Execution Context: Local Simulator (Fallback due to connection failure)")
    else:
        print("Execution Context: Live Network connected via Web3")

if __name__ == "__main__":
    main()
