"""
Main Entry Point
"""

import warnings
warnings.filterwarnings("ignore")

from src.consumer_module.train import Trainer


def main():

    print("\nSMART LOGISTICS ML PIPELINE")
    print("=" * 60)

    trainer = Trainer()

    results = trainer.train()

    print("\nTraining Completed Successfully")
    print("=" * 60)

    print(results)


if __name__ == "__main__":
    main()
