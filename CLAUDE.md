# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Bedrock Chat is a multilingual generative AI platform powered by Amazon Bedrock. Full-stack AWS-native app: React frontend, FastAPI (Python) backend running on Lambda via Lambda Web Adapter, AWS CDK infrastructure-as-code. Key features: chat conversations, custom bots with RAG (OpenSearch Serverless), bot store sharing, and agent-based task automation (Strands Agents).

## Build & Development Commands

### Frontend (`/frontend`)
- `npm ci` — install dependencies
- `npm run dev` — local dev server (requires `.env.local` from `.env.template` with CDK outputs)
- `npm run build` — production build (`tsc && vite build`)
- `npm run lint` — ESLint
- `npm test` — Vitest
- `npm run ladle` — component showcase (Ladle)

### Backend (`/backend`)
- `poetry install` — install dependencies
- `poetry run uvicorn app.main:app --reload` — local dev server
- `poetry run pytest` — run tests
- `poetry run pytest backend/tests/test_specific.py::test_name` — single test
- `poetry run mypy --config-file mypy.ini` — type checking
- `poetry run black .` — code formatting

### CDK Infrastructure (`/cdk`)
- `npm ci && npm run build` — build
- `npx cdk synth` — synthesize CloudFormation
- `npx cdk deploy --all` — deploy all stacks
- `npm test` — Jest tests

### Deployment
- `./bin.sh` — guided deployment script (supports `--disable-self-register`, `--bedrock-region`, `--cdk-json-override`)

## Pre-commit Hooks (Lefthook)

Run `lefthook install` after cloning. Hooks run in parallel:
- **Backend:** `black` (formatting) + `mypy` (type checking)
- **Frontend:** `prettier` (formatting) + `eslint` (linting)

## Architecture

### Three-tier structure
- **Frontend** (`/frontend`): React 18 + TypeScript + Vite + Tailwind CSS. Auth via AWS Amplify/Cognito. State: Zustand (global), XState (complex flows), SWR (data fetching). i18n via i18next.
- **Backend** (`/backend/app`): FastAPI on Lambda (via Lambda Web Adapter, port 8000). Routes: `conversation`, `bot`, `bot_store`, `admin`, `user`, `published_api`, `api_publication`, `global_config`. Repositories pattern for DynamoDB access. Bedrock integration for LLM calls. WebSocket support for streaming.
- **Infrastructure** (`/cdk`): CDK stacks — `bedrock-chat-stack` (main), `bedrock-custom-bot-stack` (per-bot resources), `bedrock-shared-knowledge-bases-stack` (RAG), `frontend-waf-stack` (WAF), `api-publishment-stack` (published APIs).

### AWS Services
DynamoDB (data), API Gateway + Lambda (API), CloudFront + S3 (frontend), Cognito (auth), Bedrock (LLMs), OpenSearch Serverless (RAG vector search), Step Functions (orchestration), EventBridge Pipes (events).

### Key Configuration
- `cdk.json` — deployment config (Bedrock region, WAF, IP ranges, self-signup, RAG replicas, bot store)
- `cdk/lib/constants/` — CDK constants
- `backend/app/config.py` — backend runtime config
- `frontend/.env.template` — frontend env vars template (copy to `.env.local`)

## Custom Features (NMA Fork)

Custom code is isolated in `backend/app/nma/` to minimize upstream conflicts.
- `backend/app/nma/` — custom extensions for models, logging, and deployment fixes

### Conventions
- All custom backend code goes in `backend/app/nma/` — do not create custom logic outside this folder
- Use getter functions to merge custom configs into upstream data structures
- Do not modify upstream files directly unless absolutely necessary

## Code Quality
- Do not introduce dead code (unused imports, variables, functions, or unreachable code)
- Remove any dead code you encounter while editing a file