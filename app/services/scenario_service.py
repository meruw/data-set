from pathlib import Path
from typing import List

import yaml

from app.models.scenario import Scenario


SCENARIOS_PATH = Path("scenarios")


class ScenarioService:

    @staticmethod
    def list_scenarios() -> List[str]:
        """
        Returns a list of available scenario names (file names without extension)
        """
        if not SCENARIOS_PATH.exists():
            return []

        return [
            file.stem
            for file in SCENARIOS_PATH.rglob("*.yaml")
        ]

    @staticmethod
    def load_scenario(name: str) -> Scenario:
        matches = list(SCENARIOS_PATH.rglob(f"{name}.yaml"))

        if not matches:
            raise FileNotFoundError(f"Scenario '{name}' not found")

        file_path = matches[0]

        if not file_path.exists():
            raise FileNotFoundError(f"Scenario '{name}' not found")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in scenario '{name}': {e}")

        if data is None:
            raise ValueError(f"Scenario '{name}' is empty")

        try:
            scenario = Scenario(**data)
        except Exception as e:
            raise ValueError(f"Invalid scenario structure: {e}")

        return scenario