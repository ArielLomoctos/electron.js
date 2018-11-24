const electron = require('electron');
const app = electron.app;

const BrowserWindow = electron.BrowserWindow;

var mainWindow;

// Sample run of electronJS
app.on('ready',function(){
    mainWindow = new BrowserWindow({width: 1024, height: 768, backgroundcolor: '#2e2c29'})
    // mainWindow.loadURL('file://' + __dirname + '/index.html');
    mainWindow.loadURL('https://github.com/');
});

