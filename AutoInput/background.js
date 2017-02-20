// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

var min = 1;
var max = 5;
var current = min;

function updateTitle() {
	$.ajax({
                    type: 'GET',
                    url: 'http://192.168.1.156:5000/gettitle',
                    success: function (data) {
						chrome.tabs.executeScript(null,{code:"document.getElementsByClassName('s_ipt')[0].value = '"+data.title+"'; "});
                    }
                });
	
}

chrome.browserAction.onClicked.addListener(updateTitle);
