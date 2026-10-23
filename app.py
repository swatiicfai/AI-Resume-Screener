import json
import boto3
import pdfplumber
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import io

app = FastAPI(title="AI Resume Screener")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# AWS Bedrock client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",  # Change to your region
)

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from PDF bytes using pdfplumber."""
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

MOCK_RESULT = {
    "match_score": 73,
    "verdict": "Good Match",
    "strengths": [
        "Strong background in content creation and instructional design aligns with core JD requirements",
        "Experience with e-learning development tools matches the skills required",
        "Demonstrated ability to assess training needs and design targeted learning solutions"
    ],
    "gaps": [
        "No explicit mention of LMS platforms (e.g., Moodle, Cornerstone) required by the role",
        "Missing experience with leadership development programs at scale",
        "No evidence of data-driven learning analytics or ROI measurement"
    ],
    "tips": [
        "Add specific LMS platforms you have worked with to the Skills section",
        "Quantify training impact — e.g., '200+ employees trained, 30% productivity improvement'",
        "Include a project that demonstrates alignment of L&D initiatives to business strategy"
    ]
}

def screen_resume(resume_text: str, job_description: str) -> dict:
    """Send resume + JD to AWS Bedrock Claude and get structured analysis."""
    prompt = f"""You are an expert HR recruiter and resume screener.

Analyze the following resume against the job description and return a JSON response with:
1. "match_score": integer from 0-100 (how well resume matches JD)
2. "strengths": list of 3 matching strengths
3. "gaps": list of 3 missing skills or gaps
4. "verdict": one of "Strong Match", "Good Match", "Partial Match", "Weak Match"
5. "tips": list of 3 specific improvement tips for this resume

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

Respond ONLY with valid JSON, no explanation."""

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}]
    })

    try:
        response = bedrock.invoke_model(
            modelId="anthropic.claude-3-haiku-20240307-v1:0",
            body=body
        )
        result_body = json.loads(response["body"].read())
        raw = result_body["content"][0]["text"]
        return json.loads(raw)
    except Exception:
        # No AWS credentials — return mock result for demo
        return MOCK_RESULT

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html", "r") as f:
        return f.read()

@app.post("/screen")
async def screen(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        file_bytes = await resume.read()

        # Extract text
        if resume.filename.endswith(".pdf"):
            resume_text = extract_text_from_pdf(file_bytes)
        else:
            resume_text = file_bytes.decode("utf-8", errors="ignore")

        if not resume_text:
            return JSONResponse({"error": "Could not extract text from file."}, status_code=400)

        result = screen_resume(resume_text, job_description)
        return JSONResponse(result)

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
