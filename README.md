# Travel-Agent

## 1. Clone the repository:
    ```bash
    git clone https://github.com/Paritosh025/Travel-Agent.git
    ```

## 2. Navigate to the project directory:
    ```bash
    cd Travel-Agent
    ```

## 3. Create virtual environment:
    ```bash
    conda create -n Travel-Agent python=3.11 -y
    ```

## 4. Activate the virtual environment:
    ```bash
    conda activate Travel-Agent
    ```

## 5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 6. Run the applications:
    ```bash
    python app.py
    ```



External Database URL: configure via DATABASE_URL in .env

## LangSmith tracing

Tracing is enabled when `LANGSMITH_TRACING=true` is present in `.env`.
Configure these variables with your LangSmith credentials:

```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=Travel-Agent
```

For the EU LangSmith deployment, use
`https://eu.api.smith.langchain.com` as the endpoint. Restart the application
after changing `.env`, because tracing is configured when `backend.py` loads.
