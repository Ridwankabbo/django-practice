import React, { useState } from "react";
import { useNavigate } from "react-router-dom";



const API_ENDPOINT = 'http://192.168.1.104:8000/auth-users/register-user/';

export default function Registration() {
    // return(
    //     <>
    //         <section>
    //             <form action="" className="flex flex-col py-10 gap-7">
    //                 <input type="text" name="username" id="username" placeholder="Enter username" className="px-7 py-3 rounded-xl bg-stone-100" />
    //                 <input type="email" name="email" id="email" placeholder="Enter email" className="px-7 py-3 rounded-xl bg-stone-100" />
    //                 <input type="password" name="password" id="password" placeholder="Enter password" className="px-7 py-3 rounded-xl bg-stone-100" />
    //                 <button type="submit" className="px-7 py-3 rounded-xl text-white bg-green-700">Create account</button>
    //             </form>
    //         </section>
    //     </>
    // )


    // Replace this with the actual API endpoint where you want to post the data
    

    // 1. Initialize state to hold form data
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: ''
    });

    const navigate = useNavigate();

    // 2. Handle input changes to update state
    const handleChange = (e) => {
        setFormData({
            ...formData, // Keep existing data
            [e.target.name]: e.target.value // Update the specific field
        });
    };

    // 3. Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault(); // <-- IMPORTANT: Stops the page from reloading

        console.log("Submitting data:", formData);

        try {
            const response = await fetch(API_ENDPOINT, {
                method: 'POST', // Specify the method
                headers: {
                    'Content-Type': 'application/json', // Tell the server the body is JSON
                },
                body: JSON.stringify(formData), // Convert the JS object to a JSON string
            });

            // Check if the response was successful
            if (response.ok) {
                const result = await response.json();
                console.log('Registration successful:', result);
                navigate('/verify-otp');
                // Optional: Clear form or redirect user
                setFormData({ username: '', email: '', password: '' });
                alert('Account created successfully!');
            } else {
                // Handle HTTP error responses (e.g., 400, 500)
                const errorResult = await response.json();
                console.error('Registration failed:', errorResult.message);
                alert(`Registration failed: ${errorResult.message}`);
            }

        } catch (error) {
            // Handle network errors (e.g., connection lost)
            console.error('Network or CORS error:', error);
            alert('A network error occurred. Please try again.');
        }
    };

    return (
        <>
            <section>
                {/* 4. Attach handleSubmit to the form's onSubmit event */}
                <form onSubmit={handleSubmit} className="flex flex-col py-10 gap-7">
                    {/* 5. Add value and onChange props to inputs */}
                    <input
                        type="text"
                        name="username"
                        id="username"
                        placeholder="Enter username"
                        value={formData.username}
                        onChange={handleChange}
                        className="px-7 py-3 rounded-xl bg-stone-100"
                    />
                    <input
                        type="email"
                        name="email"
                        id="email"
                        placeholder="Enter email"
                        value={formData.email}
                        onChange={handleChange}
                        className="px-7 py-3 rounded-xl bg-stone-100"
                    />
                    <input
                        type="password"
                        name="password"
                        id="password"
                        placeholder="Enter password"
                        value={formData.password}
                        onChange={handleChange}
                        className="px-7 py-3 rounded-xl bg-stone-100"
                    />
                    <button type="submit" className="px-7 py-3 rounded-xl text-white bg-green-700">
                        Create account
                    </button>
                </form>
            </section>
        </>
    )

}