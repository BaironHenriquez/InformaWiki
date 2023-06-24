// Variable para almacenar el total
let total = 0;

// Función para agregar al carrito y sumar al total
function addToCart() {
  // Verificar si el carrito ya contiene un producto
  if (total === 0) {
    // Sumar 24.990 al total
    total += 24990;

    // Actualizar el total en el HTML
    document.getElementById('cart-total').textContent = total.toFixed(2);

    // Crear el elemento de lista con el producto agregado
    const cartItem = document.createElement('li');
    cartItem.textContent = 'Suscripción Anual $24.990';

    // Agregar el elemento al carrito
    document.getElementById('cart-items').appendChild(cartItem);

    // Desactivar el botón "Agregar"
    document.getElementById('add-button').disabled = true;
  }
}

// Función para procesar el pago
function pay() {
  const paymentType = document.getElementById('payment-type').value;

  if (total > 0) {
    alert('Se ha realizado el pago con éxito.');
    console.log('Tipo de pago: ' + paymentType);
    console.log('Total a pagar: $' + total.toFixed(2));
  } else {
    alert('El carrito está vacío. No se puede realizar el pago.');
  }
}