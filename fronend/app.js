const API_BASE = "http://localhost:8000/api";

//lista inicial
async function loadPokeAPIList(query = "") {
    const listDiv = document.getElementById("pokeapi-list");
    listDiv.innerHTML = "Cargando...";
    let url = `${API_BASE}/pokemon/?limit=12`;
    if (query) {
        //buscar
        url = `${API_BASE}/pokemon/${query}`;
        try {
            const res = await fetch(url);
            if (!res.ok) throw new Error("No encontrado");
            const poke = await res.json();
            listDiv.innerHTML = "";
            listDiv.appendChild(renderPokeCard(poke));
            return;
        } catch {
            listDiv.innerHTML = "Pokémon no encontrado.";
            return;
        }
    }


    
    const res = await fetch(url);
    const data = await res.json();
    listDiv.innerHTML = "";
    for (const poke of data.results) {
        // Obtener detalles para imagen y tipos
        const pokeRes = await fetch(poke.url);
        const pokeData = await pokeRes.json();
        listDiv.appendChild(renderPokeCard(pokeData));
    }
}

//renderizar
function renderPokeCard(poke) {
    const card = document.createElement("div");
    card.className = "pokemon-card";
    card.innerHTML = `
        <img src="${poke.sprites?.front_default || ''}" alt="${poke.name}">
        <h3>${poke.name} (#${poke.id})</h3>
        <div>Tipo: ${poke.types.map(t => t.type.name).join(", ")}</div>
        <div>Peso: ${poke.weight}</div>
        <div>Altura: ${poke.height}</div>
    `;
    return card;
}

//favs
async function loadFavorites() {
    const favDiv = document.getElementById("favorites-list");
    favDiv.innerHTML = "Cargando...";
    const res = await fetch(`${API_BASE}/favorites/`);
    const data = await res.json();
    favDiv.innerHTML = "";
    if (data.length === 0) {
        favDiv.innerHTML = "<em>No tienes favoritos aún.</em>";
        return;
    }
    for (const fav of data) {
        favDiv.appendChild(renderFavoriteCard(fav));
    }
}

//rende los favs
function renderFavoriteCard(fav) {
    const card = document.createElement("div");
    card.className = "favorite-card";
    card.innerHTML = `
        <img src="${fav.image_url || 'https://placehold.co/100x100?text=No+Img'}" alt="${fav.name}">
        <h3>${fav.name} (#${fav.pokemon_id})</h3>
        <div>Entrenador: ${fav.trainer_name}</div>
        <div><em>${fav.reason || ""}</em></div>
        <div style="font-size:0.8em;color:#888;">${new Date(fav.created_at).toLocaleString()}</div>
    `;
    return card;
}

//busqueda
document.getElementById("search-form").addEventListener("submit", e => {
    e.preventDefault();
    const query = document.getElementById("search-input").value.trim().toLowerCase();
    loadPokeAPIList(query);
});



document.getElementById("favorite-form").addEventListener("submit", async e => {
    e.preventDefault();
    const name = document.getElementById("fav-name").value.trim();
    const pokemon_id = parseInt(document.getElementById("fav-id").value);
    const trainer_name = document.getElementById("trainer-name").value.trim();
    const image_url = document.getElementById("fav-image").value.trim();
    const reason = document.getElementById("fav-reason").value.trim();
    const body = { name, pokemon_id, trainer_name, image_url, reason };
    const res = await fetch(`${API_BASE}/favorites/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
    });
    if (res.ok) {
        alert("Favorito agregado!");
        loadFavorites();
        e.target.reset();
    } else {
        alert("Error");
    }
});


loadPokeAPIList();
loadFavorites();
