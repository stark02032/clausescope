# ClauseScope – AI-powered Contract Clause & Date Extractor

ClauseScope is a web application that uses Natural Language Processing (NLP) to automatically extract key clauses and important dates from contract text. It's designed to help users quickly identify critical information from legal documents without manual review.

## Features

- **Clause Extraction:** Uses dependency parsing to identify and extract meaningful clauses from the contract.
- **Date Extraction:** Accurately extracts dates in various formats using a specialized date parsing library.
- **Snippet Highlighting:** Allows users to paste snippets of the contract to see key entities (like dates, organizations, etc.) highlighted.
- **Customizable UI:** A modern and clean user interface.

## Tech Stack

- **Backend:** Python
- **Frontend:** Streamlit
- **NLP Libraries:**
    - `spaCy` for core NLP tasks and dependency parsing.
    - `dateparser` for robust date extraction.

## Local Setup and Installation

To run ClauseScope on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/stark02032/clausescope.git
    cd clausescope
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py --server.port 8501 --server.address 0.0.0.0
    ```

The application should now be open and accessible in your web browser at `http://localhost:8501`.

## Usage

1.  **Analyze a Full Contract:** Paste the entire text of your contract into the first text area and click the "Analyze Full Contract" button. The extracted clauses and dates will be displayed below.

2.  **Highlight a Snippet:** Paste a smaller portion of the contract into the second text area and click the "Highlight Snippet" button to see a version of the text with key entities highlighted.

## Deployment on Render

This application is configured for deployment on [Render](https://render.com/).

1.  **Ensure your code is pushed to GitHub:** Make sure all your changes are committed and pushed to your GitHub repository (e.g., `https://github.com/stark02032/clausescope.git`).

2.  **Create a new Web Service on Render:**
    *   Go to the [Render Dashboard](https://dashboard.render.com/).
    *   Click **"New +"** and select **"Web Service"**.
    *   Connect your GitHub account and select your `clausescope` repository.

3.  **Configure and Deploy:**
    *   Render will automatically detect your `render.yaml` file and pre-fill most of the settings.
    *   Ensure the `startCommand` is set to `sh start.sh`.
    *   Confirm the settings and click **"Create Web Service"**.

Render will then build and deploy your application. The `start.sh` script handles starting the Streamlit app with the correct port and address settings for Render's environment.

