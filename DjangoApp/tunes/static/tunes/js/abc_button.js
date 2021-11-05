// select abc-show-button
const button = document.querySelector(".abc-show-button");
const abcDisplay = document.querySelector(".abc-notation");

// function to display abc notation
const displayABC = () => {
    button.hidden = true;
    abcDisplay.hidden = false;
};

// add event listener for button
button.addEventListener("click", () => {
    displayABC();
});