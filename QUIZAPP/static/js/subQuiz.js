console.log("subQuiz.js loaded!");
const quizFormSubmit = document.getElementById("quizFormSubmit");

quizFormSubmit.addEventListener("submit", validateQuiz);

function validateQuiz(e) {
  e.preventDefault();
  // Assuming you have added the 'name' attribute to your radio buttons
  const formData = new FormData(e.target);

  // Send the data to the server using AJAX
  fetch("/submit_quiz/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "success") {
        alert(
          "Quiz submitted successfully! " +
            `Your score is ${data.score} out of ${data.totalQuestions}`
        );

        e.target.reset();
        const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0]
          .value;
          window.history.back();
      } else {
        alert("Error submitting quiz. Please try again.");
        
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Error submitting quiz. Please try again.");
    });
}

