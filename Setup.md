Setting up Brevis on your Device
=========================================

# **Installation**

## For Windows Systems

### **Installing Packages**
- Setup your conda env
    - Make sure you have Anaconda downloaded on your system. 
    ```shell
    $ conda create -n brevis python=3.6.10 
    ```

    - Download all the required packages from [**Requirements.md**](https://github.com/rahulmakhija30/brevis/blob/Version-2.0/requirements.md)

### **Dependencies Installation for frontend**
```shell
cd frontend
npm install
```

### **Starting the Application**

To start the server type the following  commands in Command Prompt:
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

Run the command to test

```
python main_serial.py
```
## For Linux Systems
### **Installing Packages**
- Setup your conda env
    - Make sure you have Anaconda downloaded on your system. 
    ```shell
    $ conda create -n brevis python=3.6.10 
    ```
    - Install node-v12.16.3

    - Download all the required packages from [**requirements.md**](https://github.com/rahulmakhija30/brevis/blob/Version-2.0/requirements.md)

### **Dependencies Installation for frontend**
```shell
cd frontend
npm install
```
### **Starting the Application**

To start the server type the following  commands in Command Prompt:
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

Run the command to test

```
python main_serial.py
```
