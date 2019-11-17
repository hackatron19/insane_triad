var synth = window.speechSynthesis;
var inputForm = document.querySelector('form');
var inputTxt = document.querySelector('#txt');
var fact=1;
var m=0;
var symptom=[];
var Uname;
var changedtext;
function speak()
{
    if (synth.speaking)
     {
        console.error('speechSynthesis.speaking');
       // $('#BadalnaHai').attr('src','C:/Users/devilal/Downloads/arya2.jpg');
        return;
         }
    if (inputTxt.value !== '')
     { 
       var utterThis = new SpeechSynthesisUtterance(inputTxt.value);
      utterThis.lang='Female(en-US)';
      utterThis.pitch=1.5;
      utterThis.rate=1;
       synth.speak(utterThis);

       utterThis.onend = function (event)
      {
        console.log('SpeechSynthesisUtterance.onend');
      }
       utterThis.onerror = function (event) 
        {
        console.error('SpeechSynthesisUtterance.onerror');
        }
     }
}
inputForm.onsubmit = function(event) {
  event.preventDefault();

  speak();

  inputTxt.blur();
}
function getUsername(){
var speech = new SpeechSynthesisUtterance();
console.log(inputTxt);
 
  speech.lang='en-US'
	speech.text = 'Hello dear, This is strange d at your service , what should i call you';
	speech.rate = 1;
	speech.pitch = 1;
  document.getElementById('txt').innerText=speech.text;
	setTimeout(()=>{synth.speak(speech);}, 1500);

	 setTimeout(()=>{recognition.start()},2500);
	}


var finalQuerry='';
var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  var recognition = new SpeechRecognition();
  recognition.continuous = true;
recognition.onresult = function(event) 
  {
   console.log('displaying search resuts');
   var current = event.resultIndex;
   var transcript = event.results[current][0].transcript;
     
     if(fact==1)
     { fact=0;
     	Uname = document.getElementById('name').innerText=transcript;
     //	Uname=$('#name').innerText;
     console.log(Uname);
     	 changedtext='Dear,'+Uname+',thanks for giving your name . here are few suggestions , you can opt to get better results. '+
     	',first one is Please be specific about your symptoms, avoid ambigious words , speak each symptom after it has been popped in the console'+
     	'Go ahead . Push the start button';
      //console.log(inputTxt);
     	  recognition.stop();
         document.getElementById('txt').innerText=changedtext;
         inputTxt.value=changedtext;
        //console.log(inputTxt)
        speak();

     }
     else
     {
     transcript+='.\n'
     $('#text').attr('value',transcript);
     finalQuerry+=transcript;
     symptom[m++]=transcript;
      document.getElementById('symptomlist').innerText=finalQuerry;
  }
}
recognition.onsoundend = function() {
  document.getElementById('symptomlist').innerText=finalQuerry;
  console.log('Sound has stopped being received\n'+finalQuerry);
 console.log(symptom);
}

$('#start-btn').on('click', function(e){
  $('#text').value='';
  console.log('hearing');
  recognition.start();
});
 $('#stop-btn').on('click',function(e){
    recognition.stop();
    console.log('stopped'+finalQuerry);
   changedtext='Dear,'+Uname+',i have accepted your symptoms, look at the symptoms in console, in case if there is anything that,'+
   ' i have misunderstood,'+'please, refresh the page and enter again . if there is no error , hit the diagonise button.';
   console.log(changedtext);
   document.getElementById('txt').innerText=changedtext;
    inputTxt.value=changedtext;
    speak();
 })

 $('#diagonise').on('click',()=>{
       
       if(symptom!='')
       { 

        $.ajax({
          method:'POST',
          url:'/symptom',
          data:{symptom:finalQuerry}
        });
       }
     });
