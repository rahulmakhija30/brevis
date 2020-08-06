### *Requirements*

> Refer [**requirements.md**](https://github.com/rahulmakhija30/brevis/blob/Version-2.0/requirements.md)


### *Dependencies Installation for frontend*
```
cd frontend
npm install
```

### *Starting the Application*

To start the server type the following  commands :
```
cd backend
python server.py
```

Open a new terminal
To start the client type the follwoing commands :
```
cd frontend
npm start
```

### **Testing Backend**

```
Install modules mentioned in requirements.md
```

Run the command to test

```
python main_serial.py
```


### *Folder Structure*
```
+
|--- frontend
|     |
|     |--- src
|            |---components
|                  |---Footer
|                       |---Footer.js
|                       |---Footer.module.css
|                  |---Home
|                       |---Home.js
|                  |---Loader
|                       |---Loader.js
|                       |---Loader.css
|                  |---Navbar
|                       |---home-run.png
|                       |---info.png
|                       |---lightbulb.png
|                       |---Nav.module.css
|                       |---sun.png
|                       |---night.png
|                       |---Navbar.js
|                  |---Stepper
|                       |---Step.module.css
|                       |---search.svg.js
|                       |---Step3.js
|                       |---Step2.js
|                       |---Step1.js
|                       |---StepComponent.js
|                  |---Functions.js
|                  |---index.js
|            |---App.js
|            |---index.css
|            |---index.js
|            |---App.module.css
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
|     |--- utils
|           |--- api_transcript.py
|           |--- clean_transcript.py
|           |--- google_speech_to_text.py
|           |--- keyframes_extractor.py
|           |--- keywords_extractor.py
|           |--- notes.py
|           |--- paragraph_headings.py
|           |--- summary_generator.py
|           |--- Transcript_Gen_API_Keys.txt
|           |--- web_scraping.py
|           |--- youtube_transcription.py
|     |--- Demo-Europarl-EN.pcl
|     |--- Image_Sim_API_Keys.txt
|     |--- main_multi.py
|     |--- main_parallel.py
|     |--- main_serial.py
|     |--- prog.py
|     |--- server.py
|     |--- server_parallel.py
|     |--- SmartStoplist.txt
|
|
|
|--- .gitignore
|
|--- README.md
|
|--- requirements.md
|
+

```
