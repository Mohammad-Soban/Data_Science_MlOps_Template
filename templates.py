import os
import logging as lg
from pathlib import Path

list_Files = [
    ".github/wokflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/Data_Ingestion.py",
    "src/components/Data_Trasnformation.py",
    "src/components/Model_Trainer.py",
    "src/components/Model_Evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/logger/logging.py",
    "src/exceptions/exceptions.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "tests/__init__.py",
    "tests/test_unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
    "README.md",
    ".gitignore"
]

def create_files():
    for file in list_Files:
        file_path = Path(file)
        file_dir, filename = os.path.split(file_path)
        if file_dir:
            os.makedirs(file_dir, exist_ok=True)
            # lg.info(f"Creating directory: {file_dir}")

        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, "w") as f:
                pass

create_files()