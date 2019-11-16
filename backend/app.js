const express=require('express');
const app =express();
const morgan=require('morgan');
const bodyp=require('body-parser');
var myPythonScript = "main.py";
var pythonExecutable = "python.exe";
const spawn = require('child_process').spawn;
var m=0;
var y
app.use(bodyp.json({type:'text/html'}));
app.use(bodyp.urlencoded({extended:true}));

app.use(express.static(__dirname+'./staticfiles/'));
app.use(morgan('dev'));
app.get('',(req,res)=>{
	console.log(__dirname+'./staticfiles');
	res.sendFile('C:/Users/devilal/Documents/strange_D_frontend/index.html')
})
app.get('/index.js',(req,res)=>{

res.sendFile('C:/Users/devilal/Documents/strange_D_frontend/staticfiles/index.js');
})
app.get('/staticfile/movingdoctor.gif',(req,res)=>{
	res.sendFile('C:/Users/devilal/Documents/strange_D_frontend/staticfiles/movingdoctor.gif');
})
app.post('/symptom',(req,res)=>{
	    y=req.body.symptom;
	    console.log(y);
       var uint8arrayToString = function(data){
      return String.fromCharCode.apply(null, data);
     };

const scriptExecution = spawn(pythonExecutable, [myPythonScript])

scriptExecution.stdout.on('data', (data) => {
    console.log(uint8arrayToString(data));
      });
var data = JSON.stringify(y);
scriptExecution.stdin.write(data);

scriptExecution.stdin.end();

scriptExecution.stderr.on('data', (data) => {
    console.log(uint8arrayToString(data));
    });

scriptExecution.on('exit', (code) => {
    console.log("Process quit with code : " + code);
});
})


app.listen(3000);
/*

var uint8arrayToString = function(data){
    return String.fromCharCode.apply(null, data);
};

//const spawn = require('child_process').spawn;
const scriptExecution = spawn(pythonExecutable, [myPythonScript])

scriptExecution.stdout.on('data', (data) => {
    console.log(uint8arrayToString(data));
});
var next="i am here. i will be everywhere"
var data = JSON.stringify(next);
scriptExecution.stdin.write(data);

scriptExecution.stdin.end();

scriptExecution.stderr.on('data', (data) => {
    console.log(uint8arrayToString(data));
});

scriptExecution.on('exit', (code) => {
    console.log("Process quit with code : " + code);
});
*/
