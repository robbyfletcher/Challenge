function findFriends(word, network) {
    network = []
    var i = 0;
    for(i = 0; i < wordList.length; i++) {
        if(word.length == wordList[i].length) {
            var j = 0;
            var diff = 0;
            for(j = 0; j < word.length; j++) {
                if(word.toLowerCase()[j] != wordList[i].toLowerCase()[j]) {
                    diff++;   
                }
            }
            if(diff == 1) {
                if(network.indexOf(wordList[i]) == -1) {
                    network.push(wordList[i]);
                }
            }
        }
        else if(Math.abs(wordList[i].length - word.length) < 2) {
            if(wordList[i].length < word.length) {
                var shorter = wordList[i];
                var longer  = word;
            }
            else {
                var shorter = word;
                var longer  = wordList[i];
            }
            var k = 0;
            var diff = 0;
            for(k = 0; k < shorter.length; k++) {
                if(shorter.toLowerCase()[k] != longer.toLowerCase()[k]) {
                    if(shorter.toLowerCase()[k] != longer.toLowerCase()[k+1]) {
                        diff++;
                    }
                }
            }
            if(diff < 1) {
                if(network.indexOf(wordList[i]) == -1) {
                    network.push(wordList[i]);
                }
            }
        }
    }
    var container;
    container = "<div id=\"friends\">" + "<b>Friends of " + word + ":</b><br><br>";
    for(i = 0; i < network.length; i++) {
        container += network[i] + "<br>";
    }
    container += "</div>";
    document.getElementById("friendsContainer").innerHTML += container;
}

function findSocialNetwork(word, network) {
    var i = 0;
    for(i = 0; i < wordList.length; i++) {
        if(word.length == wordList[i].length) {
            var j = 0;
            var diff = 0;
            for(j = 0; j < word.length; j++) {
                if(word.toLowerCase()[j] != wordList[i].toLowerCase()[j]) {
                    diff++;   
                }
            }
            if(diff == 1) {
                if(network.indexOf(wordList[i]) == -1) {
                    network.push(wordList[i]);
                    findSocialNetwork(wordList[i], network);
                }
            }
        }
        else if(Math.abs(wordList[i].length - word.length) < 2) {
            if(wordList[i].length < word.length) {
                var shorter = wordList[i];
                var longer  = word;
            }
            else {
                var shorter = word;
                var longer  = wordList[i];
            }
            var k = 0;
            var diff = 0;
            for(k = 0; k < shorter.length; k++) {
                if(shorter.toLowerCase()[k] != longer.toLowerCase()[k]) {
                    if(shorter.toLowerCase()[k] != longer.toLowerCase()[k+1]) {
                        diff++;
                    }
                }
            }
            if(diff < 1) {
                if(network.indexOf(wordList[i]) == -1) {
                    network.push(wordList[i]);
                    findSocialNetwork(wordList[i], network);
                }
            }
        }
    }
}