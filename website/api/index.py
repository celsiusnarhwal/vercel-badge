import os

import rsa
from fastapi import FastAPI
from fastapi.responses import FileResponse
from github import Github as GitHub, GithubIntegration

app = FastAPI()


@app.get("/api/{user}/{repo}")
async def get_status(user: str = None, repo: str = None):
    def authenticate(gh_user: str, gh_repo: str) -> GitHub:
        key = rsa.PrivateKey.load_pkcs1(os.getenv("GH_APP_PRIVATE_KEY"))
        pem = rsa.PrivateKey.save_pkcs1(key, format="PEM")

        integration = GithubIntegration(os.getenv("GH_APP_ID"), pem)
        install = integration.get_installation(gh_user, gh_repo)
        access = integration.get_access_token(install.id)

        return GitHub(access.token)

    file_dir = os.path.dirname(os.path.abspath(__file__))

    gh = authenticate(user, repo)
    deployment = next(d for d in gh.get_repo(f"{user}/{repo}").get_deployments()
                      if d.creator.id == int(os.getenv("VERCEL_APP_ID")))
    status = deployment.get_statuses()[0].state

    if status == "success":
        return FileResponse(os.path.join(file_dir, "assets", "badges", "ready.svg"))
    elif status in ["in_progress", "queued", "pending"]:
        return FileResponse(os.path.join(file_dir, "assets", "badges", "building.svg"))
    elif status in ["error", "failure"]:
        return FileResponse(os.path.join(file_dir, "assets", "badges", "error.svg"))
    elif status == "inactive":
        return FileResponse(os.path.join(file_dir, "assets", "badges", "canceled.svg"))


@app.get("/api/ready")
async def ready():
    return FileResponse(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "badges", "ready.svg"))


@app.get("/api/building")
async def building():
    return FileResponse(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "badges", "building.svg"))


@app.get("/api/error")
async def error():
    return FileResponse(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "badges", "error.svg"))

@app.get("/api/canceled")
async def canceled():
    return FileResponse(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "badges", "canceled.svg"))
