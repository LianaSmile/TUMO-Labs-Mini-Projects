const analyzeButton = document.getElementById("analyze-button");
const textInput = document.getElementById("text");
const letterCountSpan = document.getElementById("letter-count");
const wordCountSpan = document.getElementById("word-count");
const sentenceCountSpan = document.getElementById("sentence-count");

analyzeButton.addEventListener("click", () => {
	const text = textInput.value;
	const letterCount = getLetterCount(text);
	const wordCount = getWordCount(text);
	const sentenceCount = getSentenceCount(text);

	letterCountSpan.innerHTML = letterCount;
	wordCountSpan.innerHTML = wordCount;
	sentenceCountSpan.innerHTML = sentenceCount;
});

function getLetterCount(text) {
	return text.replace(/[^a-z]/gi, "").length;
}

function getWordCount(text) {
	return text.split(/\s+/).length;
}

function getSentenceCount(text) {
	return text.split(/[.!?]/).length - 1;
}


const randomButton = document.getElementById("random-button");

randomButton.addEventListener("click", () => {
	const r = Math.floor(Math.random() * 256);
	const g = Math.floor(Math.random() * 256);
	const b = Math.floor(Math.random() * 256);
	document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
});