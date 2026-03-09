# AI Experts Assignment (Python)

This assignment evaluates your ability to:

- set up a small Python project to run reliably (locally + in Docker),
- pin dependencies for reproducible installs,
- write focused tests to reproduce a bug,
- implement a minimal, reviewable fix.

## What you will do

### 1) Dockerfile (required)

Create a `Dockerfile` so the project can run the test suite in a non-interactive, CI-style environment.

Requirements:

- requirements.txt exists and is used during build (pip install -r requirements.txt)
- pytest must be included/pinned in requirements.txt
- The image must run tests by default (use: `CMD ["python", "-m", "pytest", "-v"]`).
- The build must install dependencies from `requirements.txt`.

### 2) requirements.txt (required)

Create a `requirements.txt` with pinned versions, using this format:

- `package==x.y.z`

### 3) README updates (required)

Update this README to include:

- how to run the tests locally,
- how to build and run tests with Docker.

### 4) Find + fix a bug (required)

There is a bug somewhere in this repository.

Your tasks:

- Identify the bug.
- Apply the smallest possible fix to make the tests pass.
- Keep the change minimal and reviewable (no refactors).

## Constraints

- Keep changes minimal and reviewable.
- Do not refactor unrelated code.
- Do not introduce extra tooling unless required.
- You may add tests and the smallest code change needed to fix the bug.

### 5) EXPLANATION.md (required)

Create `EXPLANATION.md` (max 250 words) containing:

- **What was the bug?**
- **Why did it happen?**
- **Why does your fix solve it?**
- **One realistic case / edge case your tests still don’t cover**

## How to run tests locally

1. Create a virtual environment (recommended) and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the test suite:
   ```bash
   pytest -v
   ```
   Or from the project root:
   ```bash
   python -m pytest tests/ -v
   ```

## How to build and run tests with Docker

1. Build the image:
   ```bash
   docker build -t ai-experts-assignment .
   ```
2. Run the container (tests run by default):
   ```bash
   docker run ai-experts-assignment
   ```
   The Dockerfile uses `CMD ["pytest", "-v"]`, so the test suite runs non-interactively.

## Submission

- Submit a public GitHub repository URL containing your solution to the Google form link provided.
#