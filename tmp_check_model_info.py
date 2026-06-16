import site
import sys
from pathlib import Path

site.addsitedir(str(Path(__file__).resolve().parent / "venv" / "Lib" / "site-packages"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import src.consumer_module.app.api.model_info as consumer_model_info
import src.distributor_module.app.api.model_info as distributor_model_info
import src.manufacturer_module.app.api.routes.model_info as manufacturer_model_info
import src.retailer_module.app.api.model_info as retailer_model_info
import src.farmar_module.app.api.model_info as farmer_model_info

print("consumer", consumer_model_info.__name__)
print("distributor", distributor_model_info.__name__)
print("manufacturer", manufacturer_model_info.__name__)
print("retailer", retailer_model_info.__name__)
print("farmer", farmer_model_info.__name__)
