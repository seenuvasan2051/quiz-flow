const questionsContainer = document.querySelectorAll(".questions-container");

questionsContainer.forEach(question => {
    const options = question.querySelectorAll('li');

    options.forEach(option => {
        option.addEventListener('click', (e) => {
    
            options.forEach(otherOption => {
                if (otherOption !== e.currentTarget) {
                    otherOption.classList.remove('checked');
                    otherOption.querySelector('input').checked = false;
                }
            });
            
            
            e.target.classList.add('checked');
            e.target.querySelector('input').checked  = true;
        })
    })
});

