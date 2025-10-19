import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const RESET_API = 'http://192.168.1.104:8000/auth-users/reset-password/';

export default function ResetPasswordVerify() {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [formData, setFormData] = useState({ 
        otp: '', 
        new_password: '', 
        confirm_password: '' 
    });

    // 1. Get the email that requested the reset OTP
    useEffect(() => {
        const storedEmail = localStorage.getItem('resetEmail');
        if (storedEmail) {
            setEmail(storedEmail);
        } else {
            // If email is missing, redirect back to login
            navigate('/login'); 
            alert('Please start the password reset process from the login page.');
        }
    }, [navigate]);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (formData.new_password !== formData.confirm_password) {
            alert("New passwords do not match.");
            return;
        }

        // The data payload sent to the backend
        const resetData = {
            email: email, // Email obtained from local storage
            otp: formData.otp,
            password: formData.new_password,
        };

        try {
            const response = await fetch(RESET_API, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(resetData),
            });

            const result = await response.json();

            if (response.ok) {
                alert("Password successfully reset! You can now log in.");
                localStorage.removeItem('resetEmail'); // Clear the stored email
                navigate('/login'); // Redirect to login page
            } else {
                alert(`Reset failed: ${result.message || 'Invalid OTP or email.'}`);
            }

        } catch (error) {
            console.error('Password reset error:', error);
            alert('A network error occurred during password reset.');
        }
    };

    return (
        <section className="flex flex-col py-10 gap-7 items-center">
            <h2 className="text-2xl font-bold">Reset Password</h2>
            <p className="text-gray-600">Verifying account for: **{email}**</p>
            
            <form onSubmit={handleSubmit} className="flex flex-col gap-7 w-full max-w-md">
                {/* Email Field (Read-only/Hidden) */}
                <input 
                    type="email" 
                    name="email" 
                    value={email}
                    readOnly
                    placeholder="Email" 
                    className="px-7 py-3 rounded-xl bg-gray-200 cursor-not-allowed" 
                />

                {/* OTP Field */}
                <input 
                    type="text" 
                    name="otp" 
                    placeholder="Enter OTP from Email" 
                    value={formData.otp}
                    onChange={handleChange}
                    className="px-7 py-3 rounded-xl bg-stone-100" 
                    required
                />

                {/* New Password Field */}
                <input 
                    type="password" 
                    name="new_password" 
                    placeholder="Enter New Password" 
                    value={formData.new_password}
                    onChange={handleChange}
                    className="px-7 py-3 rounded-xl bg-stone-100" 
                    required
                />
                
                {/* Confirm Password Field */}
                <input 
                    type="password" 
                    name="confirm_password" 
                    placeholder="Confirm New Password" 
                    value={formData.confirm_password}
                    onChange={handleChange}
                    className="px-7 py-3 rounded-xl bg-stone-100" 
                    required
                />

                <button 
                    type="submit" 
                    className="px-7 py-3 rounded-xl text-white bg-red-600 hover:bg-red-700"
                >
                    Reset and Log In
                </button>
            </form>
        </section>
    );
}