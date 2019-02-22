//Get Base URL
//Example : if URL is http://localhost/r/Main/Internet 
//          then, base URL is http://localhost/r/Main/
function getBaseURL() {
	var thisPageURL = window.location.href;
	if (thisPageURL === "http://localhost/r/") 
	{ 
		thisPageURL = thisPageURL + "Main/"
	}
	else {
		var enough = false;
		while (!enough) {
			var length = thisPageURL.length;
			var lastChar = thisPageURL.charAt(length-1);
			
			if (lastChar === "/") {
				enough = true
			}
			else {
				thisPageURL = thisPageURL.slice(0,-1)
			}
		}
	}
	return thisPageURL;
}

//Convert string to title case
//Example: if input is ababa
//         then, output is Ababa
function titleCaser(item) {
	var theFirst = item.charAt(0);
	theFirst = theFirst.toUpperCase();
	var theRest = item.slice(1);
	var combined = theFirst + theRest;
	return combined
}

//Shortcut Functionality
//Ctrl + . = New node
//Only work for main namespace :(
document.onkeyup = function(e) {
  if (e.ctrlKey && e.which == 190) {
  	bgdarkener = document.getElementById("bg-darkener")
  	dialogbox = document.getElementById("dialog-box")
  	console.log("a")
  	
  	console.log("b")
  	bgdarkener.style.display = "block"
  	dialogbox.style.display = "block"
  	document.getElementById("nodename").focus()
  }
  else if (e.which == 27) {
  	bgdarkener = document.getElementById("bg-darkener")
  			dialogbox = document.getElementById("dialog-box")

  			bgdarkener.style.display = "none"
  			dialogbox.style.display = "none"
  }


  else if (e.ctrlKey && e.which == 13) {
  	var node = document.getElementById("nodename");
  	var nodecontent = node.value;
  	var xhttp = new XMLHttpRequest();
  	xhttp.onreadystatechange = function(){
  		if(this.readyState == 4 && this.status == 200){
  			console.log("done")
  			var nodetext = document.getElementById("nodename")
  			nodetext.value = ""
  			bgdarkener = document.getElementById("bg-darkener")
  			dialogbox = document.getElementById("dialog-box")
  			bgdarkener.style.display = "none"
  			dialogbox.style.display = "none"
  		}
  	}
  	xhttp.open("POST","/dataGateway")
  	xhttp.send(nodecontent)
}};



