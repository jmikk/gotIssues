// ==UserScript==
// @name         AutoCloseIssuePage2
// @namespace    http://tampermonkey.net/
// @version      1.9003.3
// @description  button focus.
// @author       9003
// @match        https://www.nationstates.net/container=*/page=enact_dilemma/choice-*=1/dilemma=*/template-overall=*
// @match        https://www.nationstates.net/page=enact_dilemma/choice-*=1/dilemma=*/nation=*/template-overall=*
// @match        https://www.nationstates.net/page=enact_dilemma/choice-*=1/container=*/dilemma=*/template-overall=none
// @match        https://www.nationstates.net/page=enact_dilemma/choice-*=1/dilemma=*/nation=*/container=*/template-overall=none/pulleventmode=true
// @match        https://www.nationstates.net/page=deck/card=*/season=*/pull_event_card
// @match        https://www.nationstates.net/page=deck/card=*/season=*/close
// @updateURL    https://github.com/jmikk/gotIssues/raw/master/NsDilemmaAutoClose.user.js
// @require      https://craig.global.ssl.fastly.net/js/mousetrap/mousetrap.min.js?a4098
// @grant        window.close
// ==/UserScript==




// Your code here...
( function() {
	'use strict';
	if(!window.location.href.endsWith("/pulleventmode=true")&&!window.location.href.endsWith("/pull_event_card")&&!document.getElementsByClassName("mcollapseplain").length > 0){ window.close()};
   if(window.location.href.endsWith("/pull_event_card")){


        var stuff;
         var i;
         stuff=document.getElementsByClassName("cardprice");//[0].click();
         for (i = 0; i < stuff.length; i++)
         {
         stuff[i].click();
         }
         document.querySelector("input#new_price_value[name=\"new_price\"]").stepUp();

       //.attr("action") + "/template-overall=none"
         document.getElementById("change_price_button").setAttribute('action','location.href=https://www.nationstates.net/page=deck/card=*/season=*/close')
         document.getElementById("change_price_button").click();
    }
	if(document.getElementsByClassName("button lootboxbutton").length > 0||window.location.href.endsWith("/pull_event_card")){
		document.getElementsByClassName("button lootboxbutton")[0].focus();
	}
    else if(document.getElementsByClassName("mcollapseplain").length > 0)
    {

        //puppet = document.getElementById("entity_name").value;

        //alert('Logging '+ puppet+" in.");
        //$.post("//www.nationstates.net/", "logging_in=1&nation="+puppet+"&password="+password+"submit=Login&autologin=yes", callback);
        //alert('moving to main page');
        //window.location.replace("https://www.nationstates.net/page=deck");

    }

    else
    {window.close();}
const button=document.getElementsByClassName("button lootboxbutton")[0];
      button.addEventListener("click", (ev) => { // fires when button is clicked
            if (button.style.display == "none") {  // check if button is hidden
                ev.preventDefault();               // it is, prevent the "open pack" request from being submitted
                return;                            // return early, nothing left to do
            }

            button.style.display = "none";         // hide the button
                                                   // "open pack" request automatically submitted after this function returns
        });


    })();
