import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';

const API_ORDER_URL = 'http://localhost:8000/e-commerce/orders/';

export default function OrderSummary() {
    const location = useLocation();
    // Get the cart items passed from the Dashboard component
    const cartItems = location.state?.cartItems || {};
    
    const [orderId, setOrderId] = useState(null);
    const [invoice, setInvoice] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Prepare data for the API POST request
    const orderData = {
        items: Object.values(cartItems).map(item => ({
            product_id: item.id,
            quantity: item.quantity
        }))
    };
    
    // --- Order Placement and Invoice Fetching ---
    useEffect(() => {
        if (orderData.items.length === 0) return; // Don't proceed if cart is empty

        console.log(orderData);
        

        setLoading(true);
        setError(null);

        const placeOrder = async () => {
            try {
                // 1. PLACE ORDER (POST request)
                const response = await fetch(API_ORDER_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        // IMPORTANT: Add authorization header here if your Django backend requires authentication
                        // 'Authorization': `Token ${userToken}` 
                    },
                    body: JSON.stringify(orderData)
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.error || 'Failed to place order.');
                }

                const placedOrder = await response.json();
                setOrderId(placedOrder.id);
                
                // 2. FETCH INVOICE (GET request to retrieve the created order details)
                // Note: The POST request might already return the full invoice data (using OrderDetailSerializer)
                // but a separate GET is safer for large structures or if POST returns minimal data.
                const invoiceResponse = await fetch(`${API_ORDER_URL}${placedOrder.id}/`, {
                    headers: {
                        // Include Authorization header again
                    }
                });
                
                if (!invoiceResponse.ok) {
                    throw new Error('Order placed, but failed to fetch invoice details.');
                }
                
                const invoiceDetails = await invoiceResponse.json();
                setInvoice(invoiceDetails);

            } catch (err) {
                setError(err.message);
                console.error("Order process failed:", err);
            } finally {
                setLoading(false);
            }
        };

        placeOrder();
    }, []); // Run only once on component mount

    
    if (loading) return (
        <div className="text-center p-10">
            <p className="text-xl font-semibold">Processing Order and Generating Invoice...</p>
        </div>
    );

    if (error) return (
        <div className="text-center p-10 text-red-600">
            <h2 className="text-2xl font-bold">Error</h2>
            <p>{error}</p>
        </div>
    );
    
    if (!invoice) return (
        <div className="text-center p-10">
            <p>No cart data provided or invoice not yet generated.</p>
        </div>
    );
    
    // --- Invoice Display ---
    return (
        <div className="max-w-4xl mx-auto my-10 p-8 bg-white shadow-2xl rounded-xl">
            <h1 className="text-4xl font-extrabold mb-6 text-indigo-700 border-b pb-2">Invoice #{invoice.id}</h1>
            
            <div className="grid grid-cols-2 gap-4 mb-8 text-lg">
                <p><strong>Customer:</strong> {invoice.custommer_name || 'Guest'}</p>
                <p><strong>Order Date:</strong> {new Date(invoice.created_at).toLocaleDateString()}</p>
            </div>

            <h2 className="text-2xl font-bold mb-4 text-indigo-600">Order Items</h2>
            
            <table className="min-w-full bg-gray-50 border border-gray-200 rounded-lg overflow-hidden">
                <thead className="bg-indigo-500 text-white">
                    <tr>
                        <th className="py-3 px-6 text-left">Product</th>
                        <th className="py-3 px-6 text-right">Price</th>
                        <th className="py-3 px-6 text-right">Quantity</th>
                        <th className="py-3 px-6 text-right">Subtotal</th>
                    </tr>
                </thead>
                <tbody>
                    {invoice.items.map((item, index) => (
                        <tr key={index} className="border-b hover:bg-gray-100">
                            <td className="py-3 px-6 text-left">{item.product_name}</td>
                            <td className="py-3 px-6 text-right">${parseFloat(item.product_price).toFixed(2)}</td>
                            <td className="py-3 px-6 text-right">{item.quantity}</td>
                            <td className="py-3 px-6 text-right font-semibold">${parseFloat(item.subtotal).toFixed(2)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <div className="mt-8 text-right">
                <p className="text-3xl font-bold text-indigo-700">
                    Grand Total: ${parseFloat(invoice.total_price).toFixed(2)}
                </p>
            </div>
            
            <p className="text-center mt-10 text-gray-500 italic">Thank you for your order!</p>
        </div>
    );
}
