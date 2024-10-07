// Dynamic profile description
let profileTexts = [
    "A highly skilled full-stack developer.",
    "Passionate about solving complex problems.",
    "Experienced with React, Django, and more.",
    "Constantly learning new technologies."
];
let profileIndex = 0;

function changeProfileText() {
    const profileParagraph = document.querySelector('.profile p');
    profileParagraph.textContent = profileTexts[profileIndex];
    profileIndex = (profileIndex + 1) % profileTexts.length;
}

setInterval(changeProfileText, 3000);

// Skillset Animation
const skillset = document.querySelectorAll('.skills li');

skillset.forEach(skill => {
    skill.addEventListener('mouseover', () => {
        skill.style.backgroundColor = '#2ecc71'; // Change color on hover
    });
    skill.addEventListener('mouseout', () => {
        skill.style.backgroundColor = '#3498db'; // Revert color
    });
});
