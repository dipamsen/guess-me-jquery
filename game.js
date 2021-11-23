$(document).ready(async function () {
  // fetch wordlist.json
  const wordList = await fetch("/wordlist.json").then((res) => res.json());
  setupKeyboard();
  setupGame(wordList);
});

function setupKeyboard() {
  const keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
  keys.forEach((row) => {
    row
      .toUpperCase()
      .split("")
      .forEach((key) => {
        $("#keyboard").append(
          `<button class="key btn btn-primary m-1" data-key="${key}">${key}</button>`
        );
      });
    $("#keyboard").append("<br>");
  });
  $(".key").click(function () {
    if (gameOver) return;
    const key = this.attributes["data-key"].value;
    guess(key);
  });
}

let word;
let guessedLetters = [];
let lives = 5;
let gameOver = false;

function setupGame(wordList) {
  word = wordList[Math.floor(Math.random() * wordList.length)];
  guessedLetters = [];
  updateWord();
  $("#hint").html(word.category);
}

function guess(key) {
  if (gameOver) return;
  guessedLetters.push(key);
  if (word.word.toUpperCase().includes(key)) {
    $(`button[data-key=${key}`).addClass("btn-success");
  } else {
    $(`button[data-key=${key}`).addClass("btn-danger");
    updateLives(lives - 1);
  }
  updateWord();
}

function updateWord() {
  if (gameOver) return;
  $("#word").html(
    word.word
      .split("")
      .map((letter) =>
        guessedLetters.includes(letter.toUpperCase()) || letter === " "
          ? letter
          : "_"
      )
      .join("")
  );
  if ($("#word").html() === word.word) endGame(true);
}

function updateLives(heartCount) {
  lives = heartCount;
  const heart = "❤";
  $("#lives").html(heart.repeat(heartCount));
  if (heartCount === 0) return endGame();
}

function updateScore(newScore) {
  $("#score").html(newScore);
}

function endGame(outcome) {
  gameOver = true;
  $("#word").html(word.word);
  if (outcome) {
    $("#word").addClass("text-success");
    updateScore(word.word.length);
  } else $("#word").addClass("text-danger");
}
