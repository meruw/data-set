from app.services.scenario_service import ScenarioService


def test_load_scenario():
    scenario = ScenarioService.load_scenario("invoice_match")

    assert scenario.name == "invoice_match"
    assert len(scenario.steps) > 0