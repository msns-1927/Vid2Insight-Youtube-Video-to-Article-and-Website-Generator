# Vid2Insight-Youtube-Article-Generator

<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" /> <img src="https://img.shields.io/badge/LLM-Groq%20%7C%20LLaMA-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge" /> </p> <p align="center"> <b>Convert YouTube videos into structured articles and full websites using AI</b> </p>


## 🧠 Overview :
Vid2Insight is an AI-powered application that converts YouTube videos into structured, easy-to-read articles and optionally generates a complete website from the content. The system extracts the video transcript, processes it using a large language model, and transforms it into well-organized text with headings and sections.

The application is designed with a clean and interactive Streamlit interface, allowing users to customize output using options like tone, length, model selection, and fast mode. It also provides real-time streaming output for a better user experience and supports exporting results as a PDF or a downloadable website.

Overall, this project demonstrates how AI can be used to transform video content into reusable formats, making information more accessible and efficient to consume.

## ✨ Features :

Vid2Insight provides a complete set of features to transform video content into usable formats efficiently. The application is designed to be both powerful and user-friendly.

- **🎥 YouTube to Article Conversion :** Automatically converts any YouTube video into a clean, structured article with proper headings and sections.
- **🌐 Optional Website Generation :** Generates a complete webpage (HTML, CSS, JavaScript) from the article, which can be previewed and downloaded.
- **🎛 Customizable Controls :** Allows users to choose model, tone (professional, casual, etc.), and content length based on their needs.
- **⚡ Fast Mode Optimization :** Provides a faster generation option by reducing processing complexity.
- **💬 Real-Time Streaming Output :** Displays the generated article gradually, creating a ChatGPT-like typing experience.
- **📑 Tabbed User Interface :** Organizes output into clear sections: Article, Preview, Code, and Download for better usability.
- **📄 PDF Export (Article) :** Enables users to download the generated article as a well-formatted PDF without any code or HTML.
- **📦 Website ZIP Download :** Allows downloading the generated website files (HTML, CSS, JS) as a ZIP package.
- **🧠 Caching for Performance :** Reduces repeated processing and improves speed using caching mechanisms.
- **🌑 Modern Dark-Themed UI :** Provides a clean, centered, and visually appealing interface built with Streamlit.

## 🧰 Tech Stack :

Vid2Insight is built using a combination of modern AI, backend, and frontend technologies to create a complete end-to-end system.

**🎨 Frontend :**
- **Streamlit :** Used to build the interactive user interface. It handles user input, displays results (article, preview, code), and provides download options in a clean tab-based layout.

**🤖 AI & Backend Processing :**
- **LangChain :** Acts as the orchestration layer for working with large language models. It manages prompts, pipelines, and structured content generation.
- **Groq (LLaMA Models) :** Used as the core large language model (LLM) to process transcripts and generate structured articles and website code.

**🎥 Data Extraction :**
- **YouTube Transcript API :** Extracts captions from YouTube videos and converts them into raw text, which serves as the input for the AI model.

**📄 Export & File Handling :**
- **ReportLab :** Used to generate downloadable PDF files containing only the clean article content.
- **Zipfile (Python Standard Library) :** Used to package generated website files (HTML, CSS, JavaScript) into a downloadable ZIP archive.

**⚙️ Utilities & Supporting Tools :**
- **Python (Core Language) :** Handles overall logic, data flow, and integration between components.
- **Regex (```re``` module) :** Used to clean and process text (removing HTML/code for PDF generation).
- **Streamlit Caching (```st.cache_data```, ```st.cache_resource```) :** Improves performance by avoiding repeated computations and API calls.

**🔐 Environment Management :**
- **python-dotenv :** Loads environment variables (like API keys) securely from a ```.env``` file.

**🎯 Summary :**

This tech stack combines AI (LLMs), backend processing, and frontend UI to create a complete application that transforms video content into structured, downloadable formats efficiently.


## 🏗️ Project Architecture / Workflow :

Vid2Insight follows a clear, step-by-step pipeline that transforms a YouTube video into structured content and optional web output. The system is designed in a modular way, where each stage handles a specific responsibility.

**🔄 End-to-End Workflow :**

**1. User Input (Frontend – Streamlit) :**
The user enters a YouTube video link and selects preferences such as tone, length, model, fast mode, and whether to generate a website.

**2. Transcript Extraction (Data Layer) :**
The system uses the YouTube Transcript API to fetch captions from the video. This converts video content into raw text.

**3. Preprocessing (Backend Logic) :**
The extracted transcript is cleaned and prepared. This step removes noise and ensures the text is ready for AI processing.

**4. AI Processing (LangChain + Groq LLM) :**
The cleaned transcript is sent to the language model through LangChain.
The model:
- Understands the content
- Structures it into meaningful sections
- Generates a well-organized article

**5. Content Generation :**
- 📄 Article Generation: Produces a readable article with headings and sections
- 🌐 Website Generation (Optional): Converts the article into HTML, CSS, and JavaScript

**6. Output Rendering (Frontend) :**
The results are displayed in a tab-based UI:
- Article view (with streaming effect)
- Live webpage preview
- Source code view
- Download section

**7. Export Layer :**
- 📄 PDF Export: Generates a clean article-only PDF using ReportLab
- 📦 ZIP Export: Packages website files into a downloadable ZIP

**🧩 Component Interaction :**
The system can be understood as three main layers working together:
- Frontend (Streamlit): Handles user interaction and displays results
- Backend (Application Logic): Controls workflow and manages state
- AI Layer (LangChain + LLM): Performs content understanding and generation

**⚡ Performance Optimization :**
To ensure smooth performance:
- Caching is used to avoid repeated processing
- Fast mode reduces computation time
- Website generation is optional to save time when not needed


**🎯 Summary :**

The architecture follows a clean pipeline:

```Video → Transcript → AI Processing → Article → (Optional) Website → UI Display → Download```

This structured workflow ensures the system is efficient, scalable, and easy to understand.
