from typing import Any

from pydantic import BaseModel, Field


class StepResult(BaseModel):
    action: str = Field(..., description="Executed action name")
    success: bool = Field(..., description="Whether the step executed successfully")
    message: str | None = Field(default=None, description="Optional execution message")
    data: dict[str, Any] | None = Field(default=None, description="Optional result payload")

    model_config = {
        "extra": "forbid",
    }


class RunResult(BaseModel):
    scenario_name: str = Field(..., description="Executed scenario name")
    success: bool = Field(..., description="Whether the overall scenario execution succeeded")
    results: list[StepResult] = Field(default_factory=list, description="Step-by-step execution results")

    model_config = {
        "extra": "forbid",
    }