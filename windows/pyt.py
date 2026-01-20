#!/usr/bin/env python3
import subprocess
import time
import json

CRITICAL_SERVICES = ["Spooler", "wuauserv", "WinDefend"]
CHECK_INTERVAL = 10  # seconds


def run_powershell(command: str) -> str:
    try:
        return subprocess.check_output(
            ["powershell.exe", "-NoProfile", "-Command", command],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
    except subprocess.CalledProcessError:
        return ""


def list_services():
    cmd = "Get-Service | Select-Object Name, Status | ConvertTo-Json"
    out = run_powershell(cmd)
    if not out:
        return []
    data = json.loads(out)
    if isinstance(data, dict):
        data = [data]
    return [{"name": s["Name"], "status": s["Status"]} for s in data]


def get_service_status(name: str) -> str:
    cmd = f"Try {{ (Get-Service -Name '{name}' -ErrorAction Stop).Status }} Catch {{ 'NOT_FOUND' }}"
    return run_powershell(cmd)


def eventlog_errors(max_events: int = 10):
    cmd = (
        f"Get-WinEvent -LogName System -MaxEvents {max_events} | "
        "Where-Object {$_.LevelDisplayName -in @('Error','Warning')} | "
        "Select-Object TimeCreated, LevelDisplayName, Message | ConvertTo-Json"
    )
    out = run_powershell(cmd)
    if not out:
        return []
    data = json.loads(out)
    if isinstance(data, dict):
        data = [data]
    return data


def main():
    print("Simple Windows Service Monitoring Tool\n")

    services = list_services()
    print("Service Status (first 10):")
    for s in services[:10]:
        print(f"{s['name']} -> {s['status']}")

    logs = eventlog_errors()
    if logs:
        print("\n[EVENT LOGS - WARNING & ERROR]")
        for item in logs:
            msg = (item.get("Message") or "").replace("\r", " ").replace("\n", " ")
            print(f"{item.get('TimeCreated')} | {item.get('LevelDisplayName')} | {msg[:120]}...")

    print("\nMonitoring critical services...")
    last_state = {}
    while True:
        for service in CRITICAL_SERVICES:
            status = get_service_status(service).lower()
            prev = last_state.get(service)

            if status == "not_found":
                if prev != "not_found":
                    print(f"[WARN] Critical service not found: {service}")
                last_state[service] = "not_found"
                continue

            if status != "running" and prev != status:
                print(f"[ALERT] Critical service not running: {service} (status={status})")

            last_state[service] = status

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
