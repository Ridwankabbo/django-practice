import React from 'react';
import { Link } from 'react-router-dom';

// ProductCard receives the product data and the function to update the cart
export default function ProductCard({ id, product, onAddToCart, img }) {
    return (
        <div className="bg-white p-2 shadow-lg rounded-lg flex flex-col items-center h-85">
            <Link to={`${id}/`}>

                <h3 className="text-xl font-semibold pb-3">{product.name}</h3>
                <img src={`http://localhost:8000/${img}`} alt="" className='rounded-md pb-3' />
                <p className="text-gray-600">Price: ${product.price}</p>
                
            </Link>
            <button
                onClick={() => onAddToCart(product)}
                className="mt-3 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-200"
            >
                Add to Cart
            </button>
        </div>
    );
}
