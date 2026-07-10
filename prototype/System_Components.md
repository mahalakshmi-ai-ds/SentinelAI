# SentinelAI System Components

# Overview

SentinelAI is built as a collection of independent modules.

Each module performs one specific responsibility. This modular design makes the system easier to improve, maintain, and extend to different AI models.

## Input Safety Module

Responsibilities:

- Validate user prompts
- Detect jailbreak attempts
- Detect prompt injection
- Identify harmful requests
- Detect sensitive information

Input:
User Prompt

Output:
Validated Prompt or Risk Alert

## AI Interaction Module

Responsibilities:

- Send validated prompts to the AI model
- Receive AI responses
- Record response metadata

Supported Models (Future):

- GPT
- Claude
- Gemini
- Llama

## Response Observation Module

Responsibilities:

- Capture AI response
- Store timestamps
- Store model information
- Prepare data for evaluation

Collected Data:

- Prompt
- Response
- Model
- Time
- Session ID
  
## Risk Detection Module

This module contains multiple specialized detectors.

Detectors:

- Hallucination Detector
- Bias Detector
- Toxicity Detector
- Privacy Leakage Detector
- Ethical Risk Detector
- Medical Risk Detector
- Cybersecurity Risk Detector

Each detector generates an independent risk score.

## Sentinel Safety Score Engine

Responsibilities:

- Collect detector scores
- Apply scoring weights
- Compute final SSS
- Assign risk category

Output:

SSS = 0–100

Safety Level:

- Safe
- Low Risk
- Moderate Risk
- High Risk
  
## Recommendation Engine

Based on the SSS, the system recommends:

- Approve response
- Warn user
- Request human review
- Block response

## Dashboard Module

Displays:

- User Prompt
- AI Response
- Risk Scores
- Final SSS
- Recommendation
- Evaluation History
  
## Human Review Module

Allows reviewers to:

- Approve
- Reject
- Edit responses
- Provide feedback

## Feedback Database

Stores:

- Evaluations
- Human feedback
- Risk history
- Detector outputs

Purpose:

Support future model improvement and auditing.

## Continuous Learning Module

Future versions may use stored feedback to:

- Improve detection rules
- Adapt to emerging threats
- Refine scoring policies

User
  │
  ▼
Input Safety Module
  │
  ▼
AI Interaction Module
  │
  ▼
Response Observation
  │
  ▼
Risk Detection
  │
  ▼
SSS Engine
  │
  ▼
Recommendation Engine
  │
  ▼
Dashboard
  │
  ▼
Human Review
  │
  ▼
Feedback Database
