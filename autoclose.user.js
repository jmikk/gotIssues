// ==UserScript==
// @name         autoclose=1
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       9003
// @match        https://www.nationstates.net/page=deck/nation=*/?open_loot_box=1/autoclose=1
// @match        https://www.nationstates.net/nation=*/page=ajax3/a=junkcard/card=*/season=*/autoclose=1
// @icon         https://www.google.com/s2/favicons?sz=64&domain=nationstates.net
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    window.close();
    // Your code here...
})();
