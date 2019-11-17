const express=require('express');
const app =express();
app.set('view engine', 'ejs'); 
const morgan=require('morgan');
const path=require('path')
const bodyp=require('body-parser');
var myPythonScript = "main.py";
var pythonExecutable = "python3";
const spawn = require('child_process').spawn;
var m=0;
var y
app.use(bodyp.json({type:'text/html'}));
app.use(bodyp.urlencoded({extended:true}));
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(__dirname+'./staticfiles/'));
app.use(morgan('dev'));
app.get('',(req,res)=>{
	console.log(__dirname+'./staticfiles');
	res.sendFile('/home/gaurav/strange_D_frontend/index.html')
})

app.get('/index.js',(req,res)=>{

res.sendFile('/home/gaurav/strange_D_frontend/staticfiles/index.js');
})
app.get('/staticfile/movingdoctor.gif',(req,res)=>{
    res.sendFile('/home/gaurav/strange_D_frontend/staticfiles/movingdoctor.gif');
})
app.post('/symptom',(req,res)=>{
        y=req.body.symptom;
        
	    //console.log(y);
        var uint8arrayToString = function(data){
        return String.fromCharCode.apply(null, data);
     };

const scriptExecution = spawn(pythonExecutable, [myPythonScript])

scriptExecution.stdout.on('data', (data) => {
    console.log(uint8arrayToString(data));
    m=data;
    /*res.render('result',{disease:m},(err,html)=>{
  console.log('nowhere')
        if(err)
      throw err;
      else 
      console.log('here')  
    });*/
    //res.writeHead(200,{'Content-Type':'text/html'})
    //res.write(data);
      });
var data = JSON.stringify(y);
scriptExecution.stdin.write(data);

scriptExecution.stdin.end();

scriptExecution.stderr.on('data', (data) => {
    console.log(uint8arrayToString(data));
    m=data;
    /*res.render('result',{disease:m},(err,html)=>{
        console.log('nowhere')
        if(err)
        throw err;
        res.send(html);
    });
   // res.writeHead(200,{'Content-Type':'text/html'})
    //*/
    res.render(__dirname+"views/result.html",{disease:data});
    });

scriptExecution.on('exit', (code) => {
    console.log("Process quit with code : " + code)
    
});
//res.writeHead(200,{'Content-Type':'text/html'});
  //  res.end(m);
})
app.listen(3000);

