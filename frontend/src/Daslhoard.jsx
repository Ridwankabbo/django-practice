import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import ProductCard from "./layouts/Card"; // Renamed Card to ProductCard for clarity

export default function Dashboard() {
    const navigate = useNavigate();
    const BASE_PRODUCTS_URL = 'http://localhost:8000/e-commerce/products/';
    let CATEGORISED_PRODUCTS_URL = BASE_PRODUCTS_URL;
    const [productData, setProductData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [selectedCategory, setSelectedCategory] = useState(null);

    // CART STATE: Stores the items selected by the user
    const [cartItems, setCartItems] = useState({});

    // console.log("access Token: ",localStorage.getItem('accessToken'));
    
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

    const fileterProductByCatagory = (path)=>{
        CATEGORISED_PRODUCTS_URL += path
        console.log(CATEGORISED_PRODUCTS_URL);
        
    }

    // Calculate total quantity of items in the cart (for display)
    const totalItems = Object.values(cartItems).reduce((sum, item) => sum + item.quantity, 0);

    // --- Navigation ---
    const goToOrderPage = () => {
        // Pass the cart items via state to the Order page
        navigate('order-summary', { state: { cartItems: cartItems } });
    };

    return (
        <>
            <div className="flex justify-around bg-yellow-500 text-xl py-3 ">
                <Link to={"Car/"} onClick={fileterProductByCatagory('Cars/')} >Car</Link>
                <Link to={"food/"} onClick={fileterProductByCatagory('food/')}>Food</Link>
                <Link to={"electronic/"} onClick={fileterProductByCatagory('electronic/')}>Electronic</Link>
            </div>

            <section className="grid grid-cols-6 ">
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
                <div className="col-span-5 bg-stone-100 p-2 grid grid-cols-3 gap-4">

                    {loading ? (
                        <div>Loading products...</div>
                    ) : (
                        productData.map((item) => (
                            <ProductCard
                                key={item.id}
                                id={item.id}
                                product={item}
                                img={item.image}
                                onAddToCart={handleAddToCart}
                            />
                        ))
                    )}
                </div>
            </section>
        </>
    );
}
