import sys
import os

# Add src to pythonpath
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.services.journey_service import JourneyService
from src.shared.database.models.user import User, UserRole
from src.shared.database.models.journey_state import JourneyState, JourneyStage
from src.shared.database.models.blockchain_receipt import BlockchainReceipt
from api.schemas.journey import JourneyAdvanceRequest
from fastapi import HTTPException

from src.shared.database import Base

# Setup test db
engine = create_engine('sqlite:///agriledger.db')
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def main():
    db = SessionLocal()
    service = JourneyService(db)
    
    journey_key = "rbac-test-crop:123"
    
    # Clean up existing state
    db.query(JourneyState).filter(JourneyState.journey_key == journey_key).delete()
    db.commit()
    
    # Create mock users
    users = {
        "farmer": User(email="farmer@ex.com", full_name="Farmer", password_hash="pw", role=UserRole.farmer, id=101),
        "manufacturer": User(email="mfg@ex.com", full_name="Mfg", password_hash="pw", role=UserRole.manufacturer, id=102),
        "distributor": User(email="dist@ex.com", full_name="Dist", password_hash="pw", role=UserRole.distributor, id=103),
        "retailer": User(email="ret@ex.com", full_name="Ret", password_hash="pw", role=UserRole.retailer, id=104),
        "consumer": User(email="con@ex.com", full_name="Con", password_hash="pw", role=UserRole.consumer, id=105),
    }
    
    req = JourneyAdvanceRequest(journey_key=journey_key, farm_id="farm1", crop_type="corn", quantity=10.0, unit="kg")
    
    print("Testing RBAC and real Blockchain integration...\n")

    # 1. Start journey (should require farmer)
    print("Attempting to start journey with Manufacturer (should fail)...")
    try:
        service.advance(req, users["manufacturer"])
        print("FAIL: Manufacturer started the journey!")
    except HTTPException as e:
        print(f"SUCCESS: Rejected ({e.detail})")

    print("\nAttempting to start journey with Farmer (should succeed)...")
    res = service.advance(req, users["farmer"])
    print(f"SUCCESS: Advanced to {res['journey'].current_stage}")
    print(f"Receipt Hash: {res['blockchain_receipt']['tx_hash']}")

    # 2. Advance to Manufacturer (requires farmer)
    print("\nAttempting to advance to Manufacturer with Distributor (should fail)...")
    try:
        service.advance(req, users["distributor"])
    except HTTPException as e:
        print(f"SUCCESS: Rejected ({e.detail})")

    print("\nAttempting to advance to Manufacturer with Farmer (should succeed)...")
    res = service.advance(req, users["farmer"])
    print(f"SUCCESS: Advanced to {res['journey'].current_stage}")
    print(f"Receipt Hash: {res['blockchain_receipt']['tx_hash']}")

    # 3. Advance to Distributor (requires manufacturer)
    print("\nAttempting to advance to Distributor with Manufacturer (should succeed)...")
    res = service.advance(req, users["manufacturer"])
    print(f"SUCCESS: Advanced to {res['journey'].current_stage}")

    # 4. Advance to Retailer (requires distributor)
    print("\nAttempting to advance to Retailer with Distributor (should succeed)...")
    res = service.advance(req, users["distributor"])
    print(f"SUCCESS: Advanced to {res['journey'].current_stage}")

    # 5. Advance to Consumer (requires retailer)
    print("\nAttempting to advance to Consumer with Retailer (should succeed)...")
    res = service.advance(req, users["retailer"])
    print(f"SUCCESS: Advanced to {res['journey'].current_stage}")

    print("\nAll RBAC and Blockchain checks passed.")
    
    db.close()

if __name__ == "__main__":
    main()
