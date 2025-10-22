import React from "react";
import { Link } from "react-router-dom";

export default function Header(){
    return(
        <>
            <section className="flex justify-around items-center bg-green-700 text-white py-5">
                <div>
                    <h2 className="text-3xl">E-commerce</h2>
                </div>
                <div className="flex gap-20">
                    <Link to={'/'} className="py-3">Home</Link>
                    <Link to={'/registration'} className="bg-blue-700 text-white px-7 py-3 rounded-xl ">registratoin</Link>
                    <Link to={'/login'} className="bg-yellow-500 text-white px-7 py-3 rounded-xl">Login</Link>
                </div>
            </section>
        </>
    )
}