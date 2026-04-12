import requests

BASE_URL = "https://msdev67-email-triage-env.hf.space"

def run():
    print("[START]")

    r = requests.post(f"{BASE_URL}/reset")
    obs = r.json()
    print("[STEP] Reset:", obs)

    action = {"action": "important"}

    r = requests.post(f"{BASE_URL}/step", json=action)
    result = r.json()
    print("[STEP] Result:", result)

    print("[END] Score:", result["reward"])

if __name__ == "__main__":
    run()