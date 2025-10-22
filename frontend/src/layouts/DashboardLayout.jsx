import React from "react";
import Header from "./Header";
import { Outlet } from "react-router-dom";

export default function DashboardLayout(){
    return(
        <>
            <nav>
                <Header/>
            </nav>
            <main>
                <Outlet></Outlet>
            </main>
        </>
    )
}