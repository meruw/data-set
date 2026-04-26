from app.services.scenario_service import ScenarioService


def main():
    scenario = ScenarioService.load_scenario("invoice_match")

    print("Scenario loaded successfully")
    print(scenario.model_dump_json(indent=2))


if __name__ == "__main__":
    main()