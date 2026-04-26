from typing import Any

from pydantic import BaseModel, Field, field_validator


class ScenarioStep(BaseModel):
    action: str = Field(..., description="Action to execute, e.g. create_invoice")
    params: dict[str, Any] = Field(default_factory=dict)

    model_config = {
        "extra": "forbid",
    }

    @field_validator("action")
    @classmethod
    def validate_action_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Action cannot be empty")
        return value


class Scenario(BaseModel):
    name: str = Field(..., description="Scenario name")
    description: str | None = Field(default=None, description="Optional scenario description")
    steps: list[ScenarioStep] = Field(default_factory=list)

    model_config = {
        "extra": "forbid",
    }

    @field_validator("name")
    @classmethod
    def validate_name_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Scenario name cannot be empty")
        return value