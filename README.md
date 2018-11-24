# electron.js-app
My repository for ElectronJS applications. All documentations, coding standards, written tutorials, links, sites, and projects during the process of learning.

NON-ADMIN INSTALLATION
------------------------------------------------------------------------------------------------------------------
- Install Jupyter (non-admin)
- Open Anaconda Prompt and install NodeJS and ElectronJS <br>
`conda install -c conda-forge nodejs` <br>
`conda install -c conda-forge electron` <br>

Source(s): <br>
- https://www.anaconda.com/download/ <br>
- https://anaconda.org/conda-forge/nodejs <br>
- https://anaconda.org/conda-forge/electron <br>

ELECTRON DEPENDENCIES
------------------------------------------------------------------------------------------------------------------
This will create and download all required libs and dependencies to run electronJS application thru npm install.

- Create new folder for the application
- Run cmd: `npm init`
- Run cmd: `npm i electron-prebuilt --save-dev`
- Go to .json file then change 'Test' to 'Start'
```
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
```
- Run cmd:    `npm start`

Note: You only need to do this once and just copy/paste all downloads to a new folder.

PACKAGE ELECTRONJS APPLICATION TO .EXE
------------------------------------------------------------------------------------------------------------------
Run cmd:    `npm install -g electron-packager` <-- will be run once only (global) <br>
Run cmd:    `electron-packager .` <-- represent the current directory in your app folder (show source code) <br>
Run cmd:    `electron-packager . --asar` <-- represent the current directory in your app folder (bundled in asar) <br>
Run cmd:    `electron-packager . --all` <-- represent the current directory in your app folder (other OS) <br>
