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
const infos = document.querySelectorAll('.info');

infos.forEach((infoField) => {
  // Trouve les boutons radio associés (dans le même conteneur)
  const questionContainer = infoField.closest('.question-container');
  const radioOui = questionContainer.querySelector('.question-oui');
  const radioNon = questionContainer.querySelector('.question-non');

  // Affiche le champ conditionnel si "oui" est coché
  radioOui.addEventListener('change', () => {
    if (radioOui.checked) {
      console.log('Oui coché');
      infoField.style.display = 'block';
    }
  });

  // Masque le champ conditionnel si "non" est coché
  radioNon.addEventListener('change', () => {
    if (radioNon.checked) {
      console.log('Non coché');
      infoField.style.display = 'none';
    }
  });
});

const cartes_enfant = document.querySelectorAll('.carte-enfant');

cartes_enfant.forEach((carte_enfant) => {
  carte_enfant.addEventListener('click', () => {
    carte_enfant.classList.toggle('cliquée');
    
    const initiale = carte_enfant.querySelector('.initiale');
    const nom_enfant = carte_enfant.querySelector('.nom-enfant');
    const modification_enfant = carte_enfant.querySelector('.modification-enfant');
    
    initiale.classList.toggle('cliquée');
    nom_enfant.classList.toggle('cliquée');
    modification_enfant.classList.toggle('cliquée');
  });
});