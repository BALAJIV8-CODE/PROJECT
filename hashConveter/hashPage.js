function removeSpaces(string) {
 const newString = string.replace(/ /g, "");
 return newString;
}

function addHashtag(string) {
 const newString = removeSpaces(string);
 const words = newString.split(",");
 for (let i = 0; i < words.length; i++) {
  words[i] = "#" + words[i];
 }
 return words.join(" ");
}

function displayToDom(string) {
 document.getElementById("hashtags").innerHTML = string;
}

function buttonClick(e) {
 e.preventDefault();
 let keywords = document.getElementById("keywords").value;
 let hashtags = addHashtag(keywords);
 displayToDom(hashtags);
}
