let nibbles = 5000;
let nibblePerKey = 1;
let snippetIndex = 0;
let codeSnippets = []; 

let keyboardCost = 10;
let caffeineCost = 1000;
let nibblesPerSecond = 0; 
let monitorCost = 2000
let aiUpgradeCost = 20;
let showerCost = 5000;


let aiInterval = 2000;
let aiUpgrades = 0; 
let aiIntervalId = null; 

function upgradeAI() {
  if (nibbles >= aiUpgradeCost) {
    nibbles -= aiUpgradeCost;
    document.getElementById('nibble-count').textContent = nibbles;

    aiUpgrades++;
    aiUpgradeCost = Math.floor(aiUpgradeCost * 1.13); 
    document.getElementById('ai-upgrade-cost').textContent = aiUpgradeCost;

    if (aiIntervalId) clearInterval(aiIntervalId); 
    aiInterval = Math.max(200, aiInterval - 200); 
    aiIntervalId = setInterval(() => {
      nibbles += nibblePerKey;
      document.getElementById('nibble-count').textContent = nibbles;
    }, aiInterval);
  }
}

fetch('https://cdn.densmo.re/apphack/main.c') 
  .then(response => response.text()) 
  .then(data => {
    codeSnippets = data.split('\n'); 
  });

document.addEventListener('keyup', () => {
  if (codeSnippets.length === 0) return; 

  nibbles += nibblePerKey;
  document.getElementById('nibble-count').textContent = nibbles;

  const codeLine = codeSnippets[snippetIndex];
  snippetIndex = (snippetIndex + 1) % codeSnippets.length; 

  const output = document.getElementById('code-output');
  output.innerHTML += `<div>${codeLine}</div>`;
  output.scrollTop = output.scrollHeight;
});

function upgradeKeyboard() {
  if (nibbles >= keyboardCost) {
    nibbles -= keyboardCost;
    nibblePerKey++;
    keyboardCost = Math.floor(keyboardCost * 1.5);

    document.getElementById('nibble-count').textContent = nibbles;
    document.getElementById('upgrade-cost').textContent = keyboardCost;
  }
}

function buyExtraMonitor() {
  if (nibbles >= monitorCost) {
    nibbles -= monitorCost;
    document.getElementById('nibble-count').textContent = nibbles;

    // Double the current nibbles per second
    nibblesPerSecond *= 2;

    // Update the monitor cost
    monitorCost = Math.floor(monitorCost * 2);
    document.getElementById('monitor-cost').textContent = monitorCost;

    // Update the nibbles per second display
    document.getElementById('nibbles-per-second').textContent = `Nibbles per second: ${nibblesPerSecond}`;
  }
}
function cusumeCaffeine() {
  const caffeineButton = document.getElementById('consume-caffeine-btn');

  if (nibbles >= caffeineCost && !caffeineButton.disabled) {
    nibbles -= caffeineCost;
    document.getElementById('nibble-count').textContent = nibbles;

    const originalNibblePerKey = nibblePerKey;
    nibblePerKey += 5;
    caffeineButton.disabled = true;

    setTimeout(() => {
      nibblePerKey = originalNibblePerKey;
    }, 10000);

    setTimeout(() => {
      caffeineButton.disabled = false;
    }, 120000);

    caffeineCost = Math.floor(caffeineCost * 1.5);
    caffeineButton.textContent = `Consume Caffeine (Cost: ${caffeineCost} nibbles)`;
  }
}

function updateNibblesPerSecond() {
  const nibbleCountElement = document.getElementById('nibble-count');
  let lastNibbleCount = parseInt(nibbleCountElement.textContent);

  setInterval(() => {
    const currentNibbleCount = parseInt(nibbleCountElement.textContent);
    nibblesPerSecond = currentNibbleCount - lastNibbleCount;
    lastNibbleCount = currentNibbleCount;

    document.getElementById('nibbles-per-second').textContent = `Nibbles per second: ${nibblesPerSecond}`;
  }, 1000);
}
function takeAShower() {
  if (nibbles >= showerCost) {
    nibbles -= showerCost;
    document.getElementById('nibble-count').textContent = nibbles;

    const originalNibblePerKey = nibblePerKey;
    const originalNibblesPerSecond = nibblesPerSecond;

    nibblePerKey = Math.floor(nibblePerKey / 2);
    nibblesPerSecond = Math.floor(nibblesPerSecond / 2);

    setTimeout(() => {
      nibblePerKey = originalNibblePerKey;
      nibblesPerSecond = originalNibblesPerSecond;

      nibblePerKey = Math.floor(nibblePerKey * 1.3);
      nibblesPerSecond = Math.floor(nibblesPerSecond * 1.3);

      document.getElementById('nibbles-per-second').textContent = `Nibbles per second: ${nibblesPerSecond}`;
    }, 180000); // 3 minutes in milliseconds

    showerCost = Math.floor(showerCost * 1.5);
    document.getElementById('shower-cost').textContent = showerCost;
  }
}
updateNibblesPerSecond();