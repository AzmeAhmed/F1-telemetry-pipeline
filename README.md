# 🏎️ F1 Telemetry Pipeline 🏎️ 🏁

An independent DevOps portfolio project designed to fetch, transform, and analyze real-time and historical Formula 1 telemetry data.

This project is continuously developed in parallel with my DevOps Engineer education at **Jensen YH** to bridge software development and modern Cloud/Operations practices.

## 🛠️ Architecture & Structure
The project is built using a modular architecture to strictly separate data handling from execution:
*   `src/main.py`: The entry point of the application that executes the performance analysis.
*   `src/data_loader.py`: Contains the core logic for API requests via `FastF1`, data transformation using `Pandas`, and mathematical calculations for sector times.

---

## 📊 Telemetry Visualization
Below is the generated speed comparison chart between Lewis Hamilton (HAM) and Max Verstappen (VER), visualizing real-time metrics across the track distance:

![F1 Telemetry Output](src/f1_telemetry_output.png)

---

## ⚙️ Current Functionality (Phase 1: Completed)
The application currently performs an in-depth performance analysis between two selected drivers for any specific Grand Prix:
*   **Robust Error Handling:** Secure session loading using `try/except` blocks to gracefully handle potential API timeouts or connection drops.
*   **Sector Analysis:** Automatic conversion of sector times into `timedelta` format for precise, millisecond-accurate comparisons (Sector 1, 2, and 3).
*   **Telemetry Enrichment:** Extracts spatial telemetry data to calculate and compare the drivers' maximum speeds using `.max()`.
*   **Data Visualization:** Integrates `Matplotlib` to dynamically plot and output high-resolution telemetry graphs, mapping speed profiles directly against distance.

## 💻 How to Run the Project
1. Create a virtual environment: `python3 -m venv venv`
2. Activate the environment: `source venv/bin/activate`
3. Install dependencies: `pip install fastf1 pandas matplotlib`
4. Run the analysis: `python3 src/main.py`

---

## 🗺️ DevOps Roadmap & Future Scope
To demonstrate full lifecycle integration, this project evolves systematically through the following engineering phases:

- [x] **Phase 1: Python Core & Telemetry** (Data ingestion via FastF1, analysis with Pandas, charts via Matplotlib, and modular code architecture).
- [ ] **Phase 2: Docker & Containerization** (Packaging the Python application into an optimized Dockerfile for identical execution across all environments).
- [ ] **Phase 3: CI/CD & Automated Testing** (Implementing unit tests via pytest with automated GitHub Actions workflows running on every Pull Request).
- [ ] **Phase 4: Infrastructure as Code (IaC)** (Automated provisioning of cloud resources using Terraform for stable deployments in Azure/AWS).
- [ ] **Phase 5: Orchestration & Observability** (Deployment, scaling, and management within a live Kubernetes cluster combined with structured logging).
