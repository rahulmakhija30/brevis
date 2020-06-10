*Requirements*
```
Python version - 3.6.7
Flask version  - 0.12
npm version    - 6.14.5
```

*Dependencies Installation*
```
cd frontend
```
```
npm install
```

*Folder Structure*
```
+
|--- frontend
|     |
|     |--- src
|            |---components
|                  |---profileimages
|                  |---about.js
|                  |---About.css
|                  |---collapsible.css
|                  |---collapsible.js
|                  |---download.js
|                  |---footer.js
|                  |---home.js
|                  |---LoadingSpinner.js
|                  |---navbar.js
|                  |---Navbar.css
|                  |---Preview.css
|                  |---Preview.js
|                  |---search.svg
|            |---App.js
|            |---index.css
|            |---index.js
|            |---serviceWorker.js
|            |---setupTests.js
|     |--- node_modules
|     |--- public
|            |---favicon.ico
|            |---index.html
|            |---manifest.json
|            |---robots.txt
|     |---package-lock.json
|     |---package.json
|
|
|
|--- backend
|     |
|     |--- server.py
|     |--- youtube_transcription.py
|     |--- clean_transcript.py
|     |--- keywords_extractor.py
|     |--- summary_generator.py
|     |--- google_speech_to_text.py
|     |--- keyframes.py
|     |--- prog.py
|     |--- SmartStoplist.txt
|     |--- downloadfile.zip
|     |--- google_scrape.py
|     |--- youtube_scrape.py
|     |--- web_scraping.py
|     |--- wikipedia_summary.py
|     |--- wikipedia_sections.py
|     
|
|
|--- README
|
|--- .gitignore
|
|--- requirements.txt
|
+

```


*Starting the Application*

To start the server type the following  commands :
```
cd backend
```
```
python3 server.py
```
Open a new terminal
To start the client type the follwoing commands :
```
cd frontend
```

```
npm start
```
### **Backend**
Testing Transcription, Keywords Extraction, and Summarization

```
Install modules mentioned in requirements.txt
```

Run the command to test

```
python3 main.py
```
