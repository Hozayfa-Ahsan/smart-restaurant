/* ============================================================
   Tasty Bites - frontend logic
   - Fetches the menu from the backend
   - Manages a shopping cart
   - Sends the order to the backend
   ============================================================ */

// The cart is a map of { itemId: { ...menuItem, qty } }
const cart = {};
let menu = [];

// ---- Element references ----
const menuGrid   = document.getElementById("menu-grid");
const cartBtn    = document.getElementById("cart-btn");
const cartCount  = document.getElementById("cart-count");
const cartDrawer = document.getElementById("cart-drawer");
const cartOverlay= document.getElementById("cart-overlay");
const closeCart  = document.getElementById("close-cart");
const cartItems  = document.getElementById("cart-items");
const cartTotal  = document.getElementById("cart-total");
const checkoutForm = document.getElementById("checkout-form");
const orderMsg   = document.getElementById("order-msg");

// ---- Load the menu from the backend ----
async function loadMenu() {
  try {
    const res = await fetch("/api/menu");
    menu = await res.json();
    renderMenu();
  } catch (err) {
    menuGrid.innerHTML = "<p class='loading'>Could not load the menu. Is the server running?</p>";
  }
}

// ---- Render menu cards ----
function renderMenu() {
  menuGrid.innerHTML = "";
  menu.forEach((item) => {
    const card = document.createElement("div");
    card.className = "menu-card";
    card.innerHTML = `
      <img src="${item.image}" alt="${item.name}" />
      <div class="menu-card-body">
        <h3>${item.name}</h3>
        <p class="desc">${item.description}</p>
        <div class="menu-card-footer">
          <span class="price">$${item.price.toFixed(2)}</span>
          <button class="add-btn" data-id="${item.id}">Add +</button>
        </div>
      </div>
    `;
    menuGrid.appendChild(card);
  });

  // Wire up the "Add" buttons.
  document.querySelectorAll(".add-btn").forEach((btn) => {
    btn.addEventListener("click", () => addToCart(Number(btn.dataset.id)));
  });
}

// ---- Cart operations ----
function addToCart(id) {
  const item = menu.find((m) => m.id === id);
  if (!item) return;
  if (cart[id]) {
    cart[id].qty += 1;
  } else {
    cart[id] = { ...item, qty: 1 };
  }
  updateCart();
  openCart();
}

function changeQty(id, delta) {
  if (!cart[id]) return;
  cart[id].qty += delta;
  if (cart[id].qty <= 0) delete cart[id];
  updateCart();
}

function removeFromCart(id) {
  delete cart[id];
  updateCart();
}

// ---- Re-draw cart UI + totals ----
function updateCart() {
  const ids = Object.keys(cart);

  // Cart badge count (total quantity).
  const count = ids.reduce((sum, id) => sum + cart[id].qty, 0);
  cartCount.textContent = count;

  // Cart rows.
  if (ids.length === 0) {
    cartItems.innerHTML = "<p class='empty-msg'>Your cart is empty.</p>";
  } else {
    cartItems.innerHTML = "";
    ids.forEach((id) => {
      const item = cart[id];
      const row = document.createElement("div");
      row.className = "cart-row";
      row.innerHTML = `
        <span class="name">${item.name}</span>
        <div class="qty-controls">
          <button data-dec="${id}">−</button>
          <span>${item.qty}</span>
          <button data-inc="${id}">+</button>
        </div>
        <span class="price">$${(item.price * item.qty).toFixed(2)}</span>
        <button class="remove-btn" data-remove="${id}">🗑️</button>
      `;
      cartItems.appendChild(row);
    });

    // Wire up the row buttons.
    cartItems.querySelectorAll("[data-inc]").forEach((b) =>
      b.addEventListener("click", () => changeQty(Number(b.dataset.inc), 1)));
    cartItems.querySelectorAll("[data-dec]").forEach((b) =>
      b.addEventListener("click", () => changeQty(Number(b.dataset.dec), -1)));
    cartItems.querySelectorAll("[data-remove]").forEach((b) =>
      b.addEventListener("click", () => removeFromCart(Number(b.dataset.remove))));
  }

  // Total price.
  const total = ids.reduce((sum, id) => sum + cart[id].price * cart[id].qty, 0);
  cartTotal.textContent = total.toFixed(2);
}

// ---- Drawer open/close ----
function openCart() {
  cartDrawer.classList.add("open");
  cartOverlay.classList.add("open");
}
function closeCartDrawer() {
  cartDrawer.classList.remove("open");
  cartOverlay.classList.remove("open");
}

cartBtn.addEventListener("click", openCart);
closeCart.addEventListener("click", closeCartDrawer);
cartOverlay.addEventListener("click", closeCartDrawer);

// ---- Submit the order to the backend ----
checkoutForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  orderMsg.textContent = "";
  orderMsg.className = "order-msg";

  const items = Object.keys(cart).map((id) => ({
    id: Number(id),
    qty: cart[id].qty,
  }));

  if (items.length === 0) {
    orderMsg.textContent = "Your cart is empty.";
    orderMsg.classList.add("error");
    return;
  }

  const payload = {
    name: document.getElementById("cust-name").value,
    phone: document.getElementById("cust-phone").value,
    address: document.getElementById("cust-address").value,
    items,
  };

  try {
    const res = await fetch("/api/order", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();

    if (res.ok) {
      orderMsg.textContent = `${data.message} Order #${data.order_id} — Total $${data.total.toFixed(2)}`;
      orderMsg.classList.add("success");
      // Reset cart and form.
      Object.keys(cart).forEach((id) => delete cart[id]);
      updateCart();
      checkoutForm.reset();
    } else {
      orderMsg.textContent = data.error || "Something went wrong.";
      orderMsg.classList.add("error");
    }
  } catch (err) {
    orderMsg.textContent = "Could not reach the server.";
    orderMsg.classList.add("error");
  }
});

// ---- Start ----
loadMenu();
updateCart();
