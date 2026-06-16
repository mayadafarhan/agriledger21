import sys
import os

# Add src to pythonpath
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.services.journey_service import JourneyService
from src.shared.database.models.user import User
from src.shared.database.models.journey_state import JourneyState, JourneyStage
from src.shared.database.models.blockchain_receipt import BlockchainReceipt
from api.schemas.journey import JourneyAdvanceRequest

# Setup test db
engine = create_engine('sqlite:///agriledger.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def main():
    db = SessionLocal()
    service = JourneyService(db)
    
    # Create mock user
    user = db.query(User).first()
    if not user:
        print("No users found. Creating a test user.")
        from src.shared.database.models.user import UserRole
        user = User(email="test@example.com", full_name="Test User", password_hash="pw", role=UserRole.admin)
        db.add(user)
        db.commit()
    
    journey_key = "test-farm:test-crop:12345678"
    
    # Phase 1: Test the full flow
    stages = ["farmer", "manufacturer", "distributor", "retailer", "consumer"]
    
    for stage in stages:
        print(f"Advancing to {stage}...")
        req = JourneyAdvanceRequest(
            journey_key=journey_key,
            farm_id="test-farm",
            crop_type="test-crop",
            quantity=100.0,
            unit="kg"
        )
        try:
            result = service.advance(req, user)
            print("  State advanced. Current stage:", result["journey"].current_stage)
            if "tx_hash" in result["blockchain_receipt"]:
                print("  Receipt recorded:", result["blockchain_receipt"]["tx_hash"])
            if "id" in result["audit_event"]:
                print("  Audit logged:", result["audit_event"]["id"])
        except Exception as e:
            print("  Error:", e)
    
    # Phase 4: Persistence Test
    state = service.get_state(journey_key)
    print("\nPersistence check:")
    print("  Stage:", state.current_stage)
    print("  Completed:", state.completed)
    print("  Last Hash:", state.last_transition_hash)
    
    # Phase 3: Failure Testing
    # Test advancing a completed journey
    print("\nTesting advance on completed journey:")
    req = JourneyAdvanceRequest(journey_key=journey_key)
    result = service.advance(req, user)
    print("  Result for completed:", result["journey"].completed)
    
    db.close()

if __name__ == "__main__":
    main()
