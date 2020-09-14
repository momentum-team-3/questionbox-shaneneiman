//Event Handlers
//show add answer form on view_question
function makeAnswerFormVisable () {
    let answerFormSection = document.querySelector("#answer-form")
    let addAnswerButton = document.querySelector("#add-answer-button")
    answerFormSection.classList.remove("hidden")
    addAnswerButton.classList.add("hidden")
}

//toggle favorite question
/*
function toggleFavQuestion () {
    const questionId = toggleFavoriteLink.dataset.questionId
    fetch(`/questions/${questionId}/favorite_question/`, {
        method ="POST"
    })
    .then(res => res.json())
    .then(data => {
        if (data.favorite_question) {
            toggleFavoriteLink.innerHTML = '&#9733;'
        } else {
            toggleFavoriteLink.innerHTML = '&#9734;'
        }
    })
}
*/

//Event Listeners 
//show add answer form on view_question
let addAnswer = document.querySelector("#add-answer-button")
addAnswer.addEventListener("click", makeAnswerFormVisable)

/*
//toggle favorites
const toggleFavoriteLink = document.querySelector("#toggle-favorite")
toggleFavoriteLink.addEventListener("click", toggleFavQuestion)
*/