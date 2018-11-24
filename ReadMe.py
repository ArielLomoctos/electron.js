"""
--------------------------------------------------------------------------------
Create new folder for the application
Run cmd:    npm init
 -- this will create a .json file that contains main information of the application
 -- you need to fill out basic information

--------------------------------------------------------------------------------
Run cmd:    npm install electron --arch=ia32
 -- if this command fail run below cmd
Run cmd:    npm install --save electron

Run cmd:    npm i electron-prebuilt --save-dev <--

 -- this will install all required dependencies for the electronJs app
--------------------------------------------------------------------------------

GoTo .json file: / Change 'Test' to 'Start'

{
  "name": "electronjs",
  "version": "1.0.0",
  "description": "ElectronJs App",
  "main": "main.js",
  "scripts": {
    "start": "electron ."
  },
  "author": "Ariel.Lomoctos",
  "license": "MIT",
  "dependencies": {
    "electron": "^3.0.10"
  }
}

--------------------------------------------------------------------------------
Run cmd:    npm start


--------------------------------------------------------------------------------
PACKAGE ELECTRONJS APPLICATION
--------------------------------------------------------------------------------
Run cmd:    npm install -g electron-packager <-- will be run once only (global)
Run cmd:     electron-packager . <-- represent the current directory in your app folder (show source code)
Run cmd:     electron-packager . --asar <-- represent the current directory in your app folder (bundled in asar)
Run cmd:     electron-packager . --all <-- represent the current directory in your app folder (other OS)










"""