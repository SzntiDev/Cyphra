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
// Atrapamos el hueco que dejaste en el HTML
const eventsListContainer = document.getElementById('events-list-container');

// 1. Pedimos la información a la "compuerta 4" de Python
function loadEventsData() {
    let options = { args: ['4'] }; // Tu nuevo modo de historial

    PythonShell.run('script.py', options).then(results => {
        try {
            const historialData = JSON.parse(results[0]);
            renderEventsList(historialData); // Se lo mandamos al pintor visual
        } catch (e) {
            console.error("Error leyendo archivos de Historial:", e);
        }
    });
}

// 2. El pintor visual (crea un rectangulito por cada evento y lo inyecta)
function renderEventsList(data) {
    if (!eventsListContainer) return;
    eventsListContainer.innerHTML = ''; // Limpia el hueco por si había texto

    // Recorremos la lista que mandó Python
    // (Por defecto Python los devuelva arriba hacia abajo, puedes agregarle un data.reverse() si quieres los más nuevos arriba)
    data.reverse().forEach(evento => {
        const card = document.createElement('div');
        card.className = "bg-bg-card p-6 rounded-3xl border border-white/5 hover:border-white/10 transition-all flex items-center gap-6 group";

        // ¡Magia! Mezclamos diseño visual con tus variables (evento.titulo, evento.tipo)
        card.innerHTML = `
            <div class="w-12 h-12 bg-[#111316] rounded-2xl flex items-center justify-center group-hover:bg-brand/10 transition-all">
                <i data-lucide="zap" class="text-brand w-5 h-5"></i>
            </div>
            <div class="flex-1 space-y-1">
                <div class="flex items-center gap-3">
                    <h4 class="font-bold">${evento.titulo}</h4>
                    <span class="bg-brand/10 text-brand text-[8px] px-2 py-0.5 rounded font-extrabold uppercase">${evento.tipo}</span>
                </div>
                <p class="text-xs text-gray-500">${evento.descripcion}</p>
            </div>
            <div class="text-right space-y-1">
                <div class="text-[10px] text-gray-600 font-bold bg-[#111316] py-1 px-3 rounded-full border border-white/5 shadow-inner">
                    ${evento.fecha}
                </div>
            </div>
        `;
        eventsListContainer.appendChild(card);
    });

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
function mostrarAlerta(mensaje) {
    const modal = document.getElementById('custom-alert');
    const alertBox = document.getElementById('custom-alert-box');
    const alertMsg = document.getElementById('custom-alert-message');
    const btnAceptar = document.getElementById('custom-alert-btn');
    const fondoOscuro = document.getElementById('custom-alert-bg');

    // 1. Reemplazamos el texto por el tuyo
    alertMsg.innerText = mensaje;

    // 2. Quitamos el 'hidden' para que exista en pantalla
    modal.classList.remove('hidden');

    // 3. Pequeño truco para que haga una animación suave de entrada
    setTimeout(() => {
        alertBox.classList.remove('scale-95', 'opacity-0');
        alertBox.classList.add('scale-100', 'opacity-100');
    }, 10);

    // 4. Función para CERRAR la alerta
    const cerrarAlerta = () => {
        alertBox.classList.remove('scale-100', 'opacity-100');
        alertBox.classList.add('scale-95', 'opacity-0');

        // Esperamos 200 ms a que termine la animación antes de ocultarlo del todo
        setTimeout(() => {
            modal.classList.add('hidden');
        }, 200);

        // Limpiamos los eventos para que no se dupliquen a futuro
        btnAceptar.removeEventListener('click', cerrarAlerta);
        fondoOscuro.removeEventListener('click', cerrarAlerta);
    };

    // 5. Escuchamos el click en el botón "Aceptar" y en el fondo oscuro para cerrar
    btnAceptar.addEventListener('click', cerrarAlerta);
    fondoOscuro.addEventListener('click', cerrarAlerta);
}

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
            mostrarAlerta("Completa el sitio y el usuario.");
            return;
        } else {
            mostrarAlerta("Datos guardado con exito.");

        }

        let options = { args: ['1', length, site, user] }; // Modo 1: Generar

        PythonShell.run('script.py', options).then(messages => {
            // El script ahora imprime la contraseña y luego el mensaje de éxito
            const generatedPassword = messages[0];
            outputText.innerText = generatedPassword;
            resultBox.classList.remove('hidden');

            // Recargar bóveda automáticamente para mostrar la nueva entrada
            loadVaultData();
            loadEventsData();

        }).catch(err => {
            console.error("Error generando:", err);
            alert("Error en el motor de cifrado.");
        });
    });
}

// Inicialización
switchSection('dashboard');
loadVaultData();
loadEventsData();