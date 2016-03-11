var used = [];

function getRandNum() {
    var test = 0;
    while (test == 0) {
        test = (Math.floor(Math.random() * 26) + 1);

        for (var j = 0; j < used.length; j++) {
            if (used[j] == test) {
                test = 0;
                break;
            }
        }
        used[used.length] = test;
    }
    return test;
}

var output = "";
var formerPosition = 0;

for (var i = 0; i < 25; i++) {
    output += "<div class='grass grass" + getRandNum() + "' style='left: " + formerPosition + "px;'><" + "/div>";
    formerPosition += (Math.floor(Math.random() * 50) + 50);
}

document.write(output);
