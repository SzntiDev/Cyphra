const { PythonShell } = require('python-shell');

// 1. Navegación y Referencias
const navItems = document.querySelectorAll('.nav-item');
const sections = document.querySelectorAll('.section-content');
const vaultListContainer = document.getElementById('vault-list-container');
const activeCountDisplay = document.getElementById('active-count');

// Referencias del Panel de Detalles
const detailPanel = document.getElementById('detail-panel');
const detailEmpty = document.getElementById('detail-empty');
const detailService = document.getElementById('detail-service');
const detailUser = document.getElementById('detail-user');
const detailPass = document.getElementById('detail-pass');
const btnCopyVault = document.getElementById('btn-copy-vault');

let vaultData = []; // Guardaremos los datos aquí para no llamar a Python cada segundo

function switchSection(sectionId) {
    sections.forEach(sec => sec.classList.remove('active'));
    const targetSection = document.getElementById(sectionId);
    if (targetSection) targetSection.classList.add('active');

    navItems.forEach(item => {
        if (item.getAttribute('data-section') === sectionId) {
            item.classList.add('bg-[#1a1c1f]', 'text-brand', 'glow-brand');
            item.classList.remove('text-gray-400');
        } else {
            item.classList.remove('bg-[#1a1c1f]', 'text-brand', 'glow-brand');
            item.classList.add('text-gray-400');
        }
    });

    if (sectionId === 'vault' || sectionId === 'dashboard') {
        loadVaultData(); // Recargar datos al entrar a estas secciones
    }

    if (window.lucide) window.lucide.createIcons();
}

navItems.forEach(item => {
    item.addEventListener('click', () => switchSection(item.getAttribute('data-section')));
});

// 2. Lógica de Datos (Python API)
function loadVaultData() {
    let options = { args: ['3'] }; // Modo 3: Listar Todo

    PythonShell.run('script.py', options).then(results => {
        try {
            vaultData = JSON.parse(results[0]);
            renderVaultList(vaultData);
            updateDashboard(vaultData);
        } catch (e) {
            console.error("Error parseando JSON de Bóveda:", e);
        }
    }).catch(err => {
        console.error("Error cargando Bóveda:", err);
    });
}

function updateDashboard(data) {
    if (activeCountDisplay) {
        activeCountDisplay.innerText = data.length;
    }
}

function renderVaultList(data) {
    if (!vaultListContainer) return;
    vaultListContainer.innerHTML = ''; // Limpiar lista

    if (data.length === 0) {
        vaultListContainer.innerHTML = '<p class="text-gray-600 italic text-sm p-4">Tu bóveda está vacía.</p>';
        return;
    }

    data.forEach((item, index) => {
        const card = document.createElement('div');
        card.className = "p-6 bg-bg-card rounded-3xl border border-white/5 hover:border-brand/30 transition-all cursor-pointer group";
        card.innerHTML = `
            <div class="flex justify-between items-start mb-2">
                <h3 class="text-lg font-bold group-hover:text-brand">${item.servicio}</h3>
                <span class="bg-brand/10 text-brand text-[8px] uppercase font-extrabold px-2 py-0.5 rounded">Secure</span>
            </div>
            <p class="text-gray-500 text-xs">${item.usuario}</p>
            <div class="mt-4 flex justify-between items-center opacity-0 group-hover:opacity-100 transition-opacity">
                <span class="text-[8px] text-gray-700 font-bold uppercase tracking-widest">Ver Detalles</span>
                <i data-lucide="chevron-right" class="text-brand w-3 h-3"></i>
            </div>
        `;
        card.addEventListener('click', () => showDetail(item));
        vaultListContainer.appendChild(card);
    });

    if (window.lucide) window.lucide.createIcons();
}

function showDetail(item) {
    detailEmpty.classList.add('hidden');
    detailPanel.classList.remove('hidden');

    detailService.innerText = item.servicio;
    detailUser.innerText = item.usuario;
    detailPass.innerText = item.password;

    // Configurar botón copiar
    btnCopyVault.onclick = () => {
        navigator.clipboard.writeText(item.password);
        const icon = btnCopyVault.querySelector('i');
        // Pequeño feedback visual
        btnCopyVault.classList.add('text-brand');
        setTimeout(() => btnCopyVault.classList.remove('text-brand'), 1000);
    };
}

// 3. Lógica del Generador (Actualizada)
const btnGenerate = document.getElementById('btn-generate');
const inputSite = document.getElementById('site');
const inputUser = document.getElementById('user');
const inputLength = document.getElementById('length');
const lenValDisplay = document.getElementById('len-val');
const resultBox = document.getElementById('result-box');
const outputText = document.getElementById('output-text');

if (inputLength) {
    inputLength.addEventListener('input', () => {
        lenValDisplay.innerText = inputLength.value;
    });
}

if (btnGenerate) {
    btnGenerate.addEventListener('click', () => {
        const site = inputSite.value;
        const user = inputUser.value;
        const length = inputLength.value;

        if (!site || !user) {
            alert("Completa el sitio y el usuario.");
            return;
        }

        let options = { args: ['1', length, site, user] }; // Modo 1: Generar

        PythonShell.run('script.py', options).then(messages => {
            // El script ahora imprime la contraseña y luego el mensaje de éxito
            const generatedPassword = messages[0];
            outputText.innerText = generatedPassword;
            resultBox.classList.remove('hidden');
            
            // Recargar bóveda automáticamente para mostrar la nueva entrada
            loadVaultData();
        }).catch(err => {
            console.error("Error generando:", err);
            alert("Error en el motor de cifrado.");
        });
    });
}

// Inicialización
switchSection('dashboard');
loadVaultData();
