// ==UserScript==
// @name         autoclose=1
// @namespace    http://tampermonkey.net/
// @version      0.1
// @match        *://*/*autoclose=1
// @match        https://www.nationstates.net/*page=enact_dilemma*
// @exclude      https://www.nationstates.net/*page=show_dilemma*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=nationstates.net//
// @grant        window.close
// ==/UserScript==

// @match on autoclose=1 not necessary for gotissues but is for junkdajunk and others
// @match on enact_dilemma as autoclose does not carry over to the issue answered screen
// @exclude on show_dilemma since autoclose should not close the new intermediary screen

(function () {
    'use strict';
    window.close();
})();