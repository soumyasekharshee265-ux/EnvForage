from envforge_agent.schemas import DiagnosticReport

def _map_os_to_target(report: DiagnosticReport) -> str:
    if report.os.wsl_version:
        return "WSL"
    if "windows" in report.os.name.lower():
        return "WIN"
    return "LINUX"


def _extract_python_version(report: DiagnosticReport) -> str:
    if report.active_python:
        parts = report.active_python.version.split(".")
        return f"{parts[0]}.{parts[1]}"
    return "3.11"  # safe default