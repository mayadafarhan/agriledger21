import os
import sys

# Hardhat default account 0
os.environ["BLOCKCHAIN_RPC_URL"] = "http://127.0.0.1:8545"
try:
    with open("src/blockchain/deployed_address.txt", "r") as f:
        os.environ["BLOCKCHAIN_CONTRACT_ADDRESS"] = f.read().strip()
except Exception:
    pass
os.environ["BLOCKCHAIN_PRIVATE_KEY"] = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
os.environ["AGRILEDGER_OFFLINE_SIMULATION"] = "False"

# Now import and run the rbac test
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import test_rbac_journey_flow

if __name__ == "__main__":
    test_rbac_journey_flow.main()
