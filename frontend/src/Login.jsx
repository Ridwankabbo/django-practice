import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const LOGIN_API = 'http://localhost:8000/auth-users/login-user/';
const FORGOT_PASSWORD_API = 'http://localhost:8000/auth-users/forgot-password/';

export default function Login() {
    const [formData, setFormData] = useState({ email: '', password: '' });
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        
        // Basic check to ensure required fields are present
        if (!formData.email || !formData.password) {
            alert("Please enter both email and password.");
            return;
        }

        try {
            const response = await fetch(LOGIN_API, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData),
            });

            const result = await response.json();

            if (response.ok) {
                // Assuming the backend returns a token/user data on success
                // Save the authentication token (e.g., in localStorage)
                // localStorage.setItem('authToken', result.token); 
                alert("Login successful! Redirecting to dashboard.");
                navigate('/dashboard'); // Redirect to your main app page
            } else {
                alert(`Login failed: ${result.message || 'Invalid credentials.'}`);
            }
        } catch (error) {
            console.error('Login error:', error);
            alert('A network error occurred during login.');
        }
    };

    const handleForgotPassword = async () => {
        // Only need the email to start the process
        if (!formData.email) {
            alert("Please enter your email to reset the password.");
            return;
        }

        try {
            const response = await fetch(FORGOT_PASSWORD_API, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: formData.email }),
            });

            const result = await response.json();

            if (response.ok) {
                alert("Password reset OTP sent to your email.");
                // Store email locally to pre-fill the reset page
                localStorage.setItem('resetEmail', formData.email); 
                
                // Redirect to the combined OTP verification/password reset page
                navigate('/reset-password-verify'); 
            } else {
                alert(`Reset failed: ${result.message || 'Email not found or error occurred.'}`);
            }

        } catch (error) {
            console.error('Forgot password error:', error);
            alert('A network error occurred while requesting OTP.');
        }
    };


    return (
        <section className="flex flex-col py-10 gap-7 items-center">
            <h2 className="text-2xl font-bold">Account Login</h2>
            <form onSubmit={handleLogin} className="flex flex-col gap-7 w-full max-w-md">
                <input 
                    type="email" 
                    name="email" 
                    placeholder="Enter email" 
                    value={formData.email}
                    onChange={handleChange}
                    className="px-7 py-3 rounded-xl bg-stone-100" 
                    required
                />
                <input 
                    type="password" 
                    name="password" 
                    placeholder="Enter password" 
                    value={formData.password}
                    onChange={handleChange}
                    className="px-7 py-3 rounded-xl bg-stone-100" 
                    required
                />
                
                <button 
                    type="submit" 
                    className="px-7 py-3 rounded-xl text-white bg-green-700"
                >
                    Log In
                </button>
            </form>
            
            <button 
                type="button"
                onClick={handleForgotPassword}
                className="text-blue-600 hover:text-blue-800 text-sm mt-2"
            >
                Forgot Password?
            </button>
        </section>
    );
}