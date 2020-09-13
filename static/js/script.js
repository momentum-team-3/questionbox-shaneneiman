//Event Handler to show add answer form
function makeAnswerFormVisable () {
    let answerFormSection = document.querySelector("#answer-form")
    let addAnswerButton = document.querySelector("#add-answer-button")
    answerFormSection.classList.remove("hidden")
    addAnswerButton.classList.add("hidden")
}

//Event Listener to shower show add answer form
let newNoteNav = document.querySelector("#add-answer-button")
newNoteNav.addEventListener("click", makeAnswerFormVisable)