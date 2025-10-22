import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Card from "./layouts/Card";

export default function Dashboard() {
    const Products_URL = 'http://localhost:8000/e-commerce/products/'
    const [productData, setProductData] = useState(null)

    useEffect(() => {
        const handleProducts = async (e) => {
            try {
                const responce = await fetch(Products_URL, {
                    method: "GET",
                    // headers: {'Context-Type':'applicaton/json'}
                });


                if (responce.ok) {
                    const result = await responce.json();
                    console.log(result);

                    setProductData(result)
                }
                else {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
            }
            catch (error) {
                console.error('Login error:', error);
                alert('A network error occurred during login.');
            }
        }
        handleProducts();
    }, [])
    return (
        <>
            <section className="grid grid-cols-6 py-5">
                <div className="flex flex-col gap-5  bg-green-700 text-center text-white">
                    <Link to={'electronic/'}>Electronic</Link>
                    <Link to={'food/'}>Food</Link>
                    <Link to={'car/'}>Car</Link>

                </div>
                <div className="col-span-5 bg-stone-100 flex gap-10 flex-wrap">
                    {/* {JSON.stringify(productData, null, 2)} */}
                    {productData && productData.map((item, index)=>(
                        <Card key={item.id || index} name={item.name} image={item.image} price={item.price}/>
                    ))}
                </div>
            </section>
        </>
    )
}