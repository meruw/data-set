from fastapi import APIRouter, HTTPException

from app.services.scenario_service import ScenarioService

router = APIRouter(prefix="/scenarios", tags=["scenarios"])


@router.get("")
def list_scenarios():
    return {
        "scenarios": ScenarioService.list_scenarios()
    }


@router.get("/{name}")
def get_scenario(name: str):
    try:
        return ScenarioService.load_scenario(name)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Scenario '{name}' not found")
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))