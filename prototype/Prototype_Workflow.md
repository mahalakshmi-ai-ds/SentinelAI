# SentinelAI Prototype Workflow

## Objective

The SentinelAI prototype demonstrates how an AI system can be continuously monitored after deployment.

Instead of only generating responses, SentinelAI observes AI behaviour, evaluates multiple safety risks, calculates a Sentinel Safety Score (SSS), and provides recommendations before the response reaches the user.

---

# Overall Workflow

User Prompt

↓

Input Safety Validation

↓

AI Model Response

↓

Response Observation

↓

Risk Detection Engine

↓

Sentinel Safety Score (SSS)

↓

Recommendation Engine

↓

Dashboard

↓

Human Review (if necessary)

↓

Feedback Database

## Step 1 — User Prompt

The user submits a prompt to the AI system.

Example:

"Can I ignore chest pain?"

The prompt is forwarded to the Input Safety Layer.

---

## Step 2 — Input Safety Validation

The prompt is analyzed before reaching the AI.

Checks include:

- Prompt Injection
- Jailbreak Attempts
- Harmful Requests
- Sensitive Information
- Malicious Instructions

If dangerous, the request is flagged.

Otherwise, it proceeds.

---

## Step 3 — AI Response Generation

The AI model generates a response.

Example:

"Chest pain is usually harmless."

The response is NOT immediately sent to the user.

Instead, SentinelAI evaluates it.

---

## Step 4 — Response Observation

SentinelAI records:

- User Prompt
- AI Response
- Timestamp
- Model Name
- Session ID
- Confidence Score

This creates an evaluation record.

---

## Step 5 — Risk Detection

Multiple detectors independently analyze the response.

Detectors include:

- Hallucination Detector
- Bias Detector
- Privacy Detector
- Toxicity Detector
- Ethical Risk Detector
- Medical Risk Detector
- Cybersecurity Detector

Each detector produces a risk score.

---

## Step 6 — Sentinel Safety Score (SSS)

All detector scores are combined.

Example:

Hallucination = 10

Bias = 4

Privacy = 0

Medical = 22

Cybersecurity = 0

Overall SSS = 86 / 100

Higher scores indicate safer responses.

---

## Step 7 — Recommendation Engine

Based on the SSS:

90–100 → Safe

75–89 → Low Risk

50–74 → Moderate Risk

Below 50 → Human Review Required

The recommendation is attached to the response.

---

## Step 8 — Dashboard

The dashboard displays:

- Prompt
- Response
- Individual Risk Scores
- Overall SSS
- Safety Recommendation
- Risk History
- Trends

Researchers can monitor AI behaviour in real time.

---

## Step 9 — Human Review

Responses with low SSS are reviewed by humans.

Experts can:

- Approve
- Reject
- Correct
- Add Feedback

Their decisions improve future evaluations.

---

## Step 10 — Continuous Learning

All evaluation results are stored.

The prototype learns:

- New attack patterns
- New hallucinations
- New jailbreak methods
- Human corrections

This enables continuous improvement.

# Prototype Goals

The prototype aims to demonstrate:

- Continuous AI monitoring
- Multi-dimensional safety evaluation
- Sentinel Safety Score generation
- Human-in-the-loop review
- Explainable AI safety decisions

This prototype serves as a proof of concept for future research and real-world deployment.

# Future Implementation

Future versions of SentinelAI will support:

- OpenAI models
- Anthropic Claude
- Gemini
- Llama
- Multi-agent AI systems
- Enterprise AI deployments
- Real-time dashboards
- API integration

↓

Continuous Learning
