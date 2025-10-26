import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import ProductCard from "./layouts/Card"; // Renamed Card to ProductCard for clarity

export default function Dashboard() {
    const navigate = useNavigate();
    const BASE_PRODUCTS_URL = 'http://localhost:8000/e-commerce/products/';
    const [productData, setProductData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [selectedCategory, setSelectedCategory] = useState(null);
    
    // CART STATE: Stores the items selected by the user
    const [cartItems, setCartItems] = useState({}); 

    // --- Data Fetching Logic (Same as before) ---
    useEffect(() => {
        setLoading(true);
        let fetchUrl = BASE_PRODUCTS_URL;
        if (selectedCategory) {
            fetchUrl = `${BASE_PRODUCTS_URL}?catagory=${selectedCategory}`;
        }
        
        const handleProducts = async () => {
            // ... (Your existing fetch logic) ...
            try {
                const response = await fetch(fetchUrl);
                const result = await response.json();
                setProductData(result);
            } catch (error) {
                console.error('Fetch error:', error);
            } finally {
                setLoading(false);
            }
        };
        handleProducts();
    }, [selectedCategory]); 

    // --- Cart Management Functions ---
    const handleAddToCart = (product) => {
        setCartItems(prevCart => {
            const productId = product.id;
            
            // Create a new cart object with updated quantity
            return {
                ...prevCart,
                [productId]: {
                    ...product, // Store full product info (name, price)
                    quantity: (prevCart[productId]?.quantity || 0) + 1
                }
            };
        });
    };

    // Calculate total quantity of items in the cart (for display)
    const totalItems = Object.values(cartItems).reduce((sum, item) => sum + item.quantity, 0);

    // --- Navigation ---
    const goToOrderPage = () => {
        // Pass the cart items via state to the Order page
        navigate('dashboard/order-summary', { state: { cartItems: cartItems } });
    };

    return (
        <section className="grid grid-cols-6 py-5">
            {/* Sidebar for Category Selection and Cart Summary */}
            <div className="flex flex-col gap-5 bg-green-700 text-center text-white p-4">
                {/* Category buttons here... */}
                
                <h3 className="text-2xl mt-10">🛒 Cart Summary</h3>
                <p className="text-lg">Total Items: {totalItems}</p>
                
                {totalItems > 0 && (
                    <button 
                        onClick={goToOrderPage}
                        className="bg-yellow-400 hover:bg-yellow-500 text-black font-bold py-2 px-4 rounded transition duration-200"
                    >
                        Proceed to Order ({totalItems})
                    </button>
                )}
            </div>

            {/* Product Display Area */}
            <div className="col-span-5 bg-stone-100 p-4 grid grid-cols-3 gap-4">
                {loading ? (
                    <div>Loading products...</div>
                ) : (
                    productData.map((item) => (
                        <ProductCard 
                            key={item.id} 
                            product={item}
                            img={item.image}
                            onAddToCart={handleAddToCart}
                        />
                    ))
                )}
            </div>
        </section>
    );
}
