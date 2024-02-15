const quizForm = document.getElementById("quizForm");

if(quizForm)
    quizForm.addEventListener('submit', createQuiz)

function createQuiz(e) {
  e.preventDefault();
  const formData = new FormData(e.target);

  // Validate form fields
  const quizType = formData.get("quiz_type");
  const questionText = formData.get("question_text");
  const option1 = formData.get("option1");
  const option2 = formData.get("option2");
  const option3 = formData.get("option3");
  const option4 = formData.get("option4");
  const correctOption = formData.get("correct_option");

  if (
    !quizType ||
    !questionText ||
    !option1 ||
    !option2 ||
    !option3 ||
    !option4 ||
    !correctOption
  ) {
    alert("Please fill in all fields");
    return;
  }

  // Additional validation logic if needed

  // Proceed with form submission
  fetch("/create_quiz/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "success") {
        alert("Quiz created successfully");
        // You can optionally reset the form after successful submission
        e.target.reset();
      } else {
        alert("Error creating quiz: " + data.message);
      }
    })
    .catch((error) => {
      console.error("Error creating quiz:", error);
    });
}
