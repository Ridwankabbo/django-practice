import React from "react";

export default function Card({ name, image, price }) {
    return (
        <>
            <div className="p-3 flex flex-col gap-5 items-center bg-white m-5 rounded-xl">
                <div className="text-center">
                    <h2 className="text-2xl font-bold">{name}</h2>
                    <img src={`http://localhost:8000/${image}`} alt="image" className="rounded-xl" />
                    <h5>Price:{price}</h5>

                </div>
                <div>
                    <button className="px-6 py-3 bg-yellow-500 text-white rounded-sm">Buy</button>
                </div>
            </div>
        </>
    )
}