// Sélectionner toutes les cartes
const carte_btns = document.querySelectorAll('.carte-border');

// Ajouter un événement de clic à chaque carte
carte_btns.forEach((carte_btn) => {
  carte_btn.addEventListener('click', () => {
    // Toggle la classe 'cliquée' sur la carte cliquée
    carte_btn.classList.toggle('cliquée');
    
    // Appliquer ou retirer la classe 'cliquée' pour les autres éléments de la carte
    const carte = carte_btn.querySelector('.carte');
    const barre_camp = carte_btn.querySelectorAll('.barre-camp');
    const carte_camp = carte_btn.querySelector('.carte-camp');
    const carte_adresse = carte_btn.querySelector('.carte-adresse');
    const participation = carte_btn.querySelector('.participation');
    
    carte.classList.toggle('cliquée');
    barre_camp.forEach(element => {
        element.classList.toggle('cliquée');
    });
    carte_camp.classList.toggle('cliquée');
    carte_adresse.classList.toggle('cliquée');
    participation.classList.toggle('cliquée');
  });
});

const participation_btn = document.querySelectorAll('.participation');

function effet(event){
    event.target.style.color = '#E17909';
    event.target.style.cursor = 'pointer';
}

function normal(event){
    event.target.style.color = '';
    event.target.style.cursor = '';
}

participation_btn.forEach(bouton => {
    bouton.addEventListener('mouseover',effet);
    bouton.addEventListener('mouseout',normal);

});

const toggleFields = [
  { radioYes: 'case-cardiaque', radioNo: 'case-cardiaque-non', textField: 'cardiaque-info' },
  { radioYes: 'case-respiratoire', radioNo: 'case-respiratoire-non', textField: 'respiratoire-info' },
  { radioYes: 'case-medicament', radioNo: 'case-medicament-non', textField: 'medicament-info' },
  { radioYes: 'case-alimentaire', radioNo: 'case-alimentaire-non', textField: 'alimentaire-info' },
];

toggleFields.forEach(({ radioYes, radioNo, textField }) => {
  const yesButton = document.getElementById(radioYes);
  const noButton = document.getElementById(radioNo);
  const field = document.getElementById(textField);

  yesButton.addEventListener('change', () => {
    if (yesButton.checked) {
      field.style.display = 'block';
    }
  });

  noButton.addEventListener('change', () => {
    if (noButton.checked) {
      field.style.display = 'none';
    }
  });
});