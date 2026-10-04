from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(title="Project Management MVP")


@app.get("/", response_class=HTMLResponse)
async def home() -> str:
    return """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Project Management MVP</title>
  </head>
  <body>
    <main>
      <h1>Hello, world</h1>
      <p>The backend is running locally.</p>
    </main>
  </body>
</html>"""


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
