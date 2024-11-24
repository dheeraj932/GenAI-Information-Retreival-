# GenAI Information Retrieval System 🤖

A Streamlit-based application that allows users to upload PDF documents and ask questions about their content using Google's Generative AI.

## Features

- 📄 PDF Document Upload: Support for multiple PDF files
- 💬 Interactive Q&A: Ask questions about your documents
- 🔍 Smart Search: Uses FAISS for efficient document retrieval
- 🧠 AI-Powered: Powered by Google's Generative AI
- 💻 User-Friendly Interface: Built with Streamlit

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/GenAI-Information-Retreival-.git
   cd GenAI-Information-Retreival-
   ```
2. Create and activate a virtual environment:
   ```
   conda create -n genai python=3.9
   conda activate genai
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   
## Usage

1. Start the application:
   ```
   streamlit run app.py
   ```
2. Upload PDF documents using the sidebar
3. Click "Submit & Process" to process the documents
4. Ask questions about your documents in the text input field

## Project Structure
```
├── src/
│ ├── init.py
│ └── helper.py # Core functionality
├── app.py # Streamlit application
├── requirements.txt # Project dependencies
├── setup.py # Package configuration
├── template.py # Project structure template
└── .env # Environment variables
```

## Dependencies

- python-dotenv
- google-generativeai
- langchain
- PyPDF2
- faiss-cpu
- streamlit

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Generative AI
- Langchain
- Streamlit
- FAISS (Facebook AI Similarity Search)

## Note

Make sure to keep your Google API key confidential and never commit it directly to the repository. Always use environment variables for sensitive information.
