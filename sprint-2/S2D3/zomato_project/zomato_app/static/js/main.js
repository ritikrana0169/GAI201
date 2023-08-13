document.addEventListener("DOMContentLoaded", function () {
    const menuList = document.getElementById("menu-list");
    const ordersList = document.getElementById("orders-list");

    // Sample menu data (replace with actual data from JSON)
    const menuData = [
        { dish_id: 1, dish_name: "Pasta", price: 10.99, is_available: true },
        { dish_id: 2, dish_name: "Burger", price: 7.99, is_available: true }
    ];

    // Sample orders data (replace with actual data from JSON)
    const ordersData = [
        { order_id: 1, customer_name: "John", dish_ids: [1], status: "received" },
        { order_id: 2, customer_name: "Alice", dish_ids: [2], status: "preparing" }
    ];

    // Function to populate menu items
    function populateMenu() {
        menuData.forEach(item => {
            const li = document.createElement("li");
            li.textContent = `${item.dish_name} - $${item.price}`;
            menuList.appendChild(li);
        });
    }

    // Function to populate orders
    function populateOrders() {
        ordersData.forEach(order => {
            const li = document.createElement("li");
            li.textContent = `Order #${order.order_id} - ${order.customer_name} (${order.status})`;
            ordersList.appendChild(li);
        });
    }

    // Call the functions to populate menu and orders
    populateMenu();
    populateOrders();

    // Implement interactive features as needed
});
