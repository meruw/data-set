# Fastbank Demo Data Tool

## Overview

Fastbank Demo Data Tool is an internal utility designed to generate realistic, scenario-based data for training, testing, and demonstrating Fastbank workflows integrated with SAP Business One.

The tool automates the creation of SAP entities (such as Business Partners and Invoices) and generates external transaction fixtures (e.g., CSV files) to simulate real-world financial scenarios across different Fastbank modules.

This enables consistent, repeatable demo environments without relying on manually created data.

---

## Problem

During client trainings and internal demos, the lack of consistent and complete datasets limits the ability to fully showcase Fastbank functionality.

Common issues include:

* Missing or incomplete SAP data (Business Partners, Invoices)
* Inability to reproduce specific reconciliation scenarios
* Manual setup being time-consuming and error-prone
* Inconsistent demo experiences across sessions

---

## Solution

This tool provides:

* Scenario-based data generation using YAML configuration files
* Automated seeding of SAP Business One data via Service Layer
* Generation of external transaction files (CSV / NACHA)
* A simple interface (CLI + Web UI) to execute scenarios
* A reusable and scalable approach to demo data management

---

## Key Features

* **Scenario-driven architecture**
  Define complete demo setups using YAML files

* **SAP B1 integration**
  Create Business Partners, Invoices, and other entities via Service Layer

* **Transaction fixture generation**
  Generate CSV (and future NACHA) files for bank transactions

* **API-first design**
  Backend designed to support future UI migration (e.g., Angular)

* **CLI and Web UI**
  Run scenarios via command line or browser

* **Dockerized environment**
  Easy to run and reproduce across environments

---

## Architecture

The system is designed with a modular, API-first architecture:

* **Core Engine**
  Scenario runner, seeders, and validators

* **Clients**
  SAP Service Layer integration

* **Fixtures**
  CSV / NACHA generators

* **Interfaces**

  * CLI (developer usage)
  * Web UI (internal usage)
  * REST API (future integrations / Angular UI)

---

## Project Structure

```
app/
  api/           # FastAPI routes
  cli/           # CLI entrypoint
  core/          # config, logging
  clients/       # SAP / external integrations
  models/        # data models
  services/      # business logic
  runner/        # scenario execution
  seeders/       # SAP data creation
  fixtures/      # CSV / NACHA generation
  validators/    # validations
  web/           # UI (v1, Bootstrap)

scenarios/       # YAML scenario definitions
output/          # generated files and logs
```

---

## Getting Started

### Prerequisites

* Docker
* Docker Compose

### Setup

```bash
git clone https://github.com/meruw/data-set
cd fb-demo-data
cp .env.example .env
```

### Run the application

```bash
docker compose up --build
```

### Access the API

```
http://localhost:8000/health
```

---

## Usage

### List scenarios

```bash
python app/main.py list
```

### Run a scenario

```bash
python app/main.py seed --scenario <scenario_name>
```

### API example

```http
POST /api/scenarios/{name}/seed
```

---

## Scenarios

Scenarios are defined using YAML files and describe:

* SAP entities to create (Business Partners, Invoices, etc.)
* External transaction data (CSV / NACHA)
* Expected outcomes (for validation)

Example:

```yaml
name: invoice_match

sap:
  business_partners:
    - CardCode: DEMO_BP_001
      CardName: Demo BP

  invoices:
    - CardCode: DEMO_BP_001
      DocumentLines:
        - ItemCode: A00001
          Quantity: 1
          UnitPrice: 1500

external:
  csv_import:
    rows:
      - description: "Payment DEMO_BP_001"
        amount: 1500
        date: "2026-04-19"
```

---

## Roadmap

* [ ] SAP data seeding (BP, Invoices, Payments)
* [ ] CSV transaction generation
* [ ] NACHA file generation
* [ ] Web UI (Bootstrap v1)
* [ ] Scenario validation layer
* [ ] Angular UI (future)
* [ ] CI/CD pipeline (lint, tests, Docker build)

---

## Contributing

This project is intended as an internal tool. Contributions should focus on:

* New scenarios
* Improved seeders
* Better validation logic
* Additional integrations

---

## Notes

* This tool interacts with SAP Business One via Service Layer
* Intended for demo and testing environments only
* Not designed for production financial operations

---

## Author

Internal Fastbank Engineering Tool
Developed as part of QA → Engineering initiative
