import React from 'react';

// ProductCard receives the product data and the function to update the cart
export default function ProductCard({ product, onAddToCart, img }) {
    return (
        <div className="bg-white p-4 shadow-lg rounded-lg flex flex-col items-center">
            <h3 className="text-xl font-semibold">{product.name}</h3>
            <img src={`http://localhost:8000/${img}`} alt="" />
            <p className="text-gray-600">Price: ${product.price}</p>
            {/*  */}
            <button 
                onClick={() => onAddToCart(product)}
                className="mt-3 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-200"
            >
                Add to Cart
            </button>
        </div>
    );
}
