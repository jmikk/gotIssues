// ==UserScript==
// @name         autoclose=1
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       9003
// @match         *://*/*autoclose=1
// @exclude      https://www.nationstates.net/*page=show_dilemma*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=nationstates.net// 
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    window.close();
    // Your code here...
})();
