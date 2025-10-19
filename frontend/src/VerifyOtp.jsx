import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

// Replace with your actual OTP verification endpoint
const VERIFY_OTP_ENDPOINT = 'http://192.168.1.104:8000/auth-users/verify-opt/'; 

export default function VerifyOtp() {
    const [email, setEmail] = useState('')
    const [otp, setOtp] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        // email or ID along with the OTP. For simplicity here, we only send the OTP.
        const verificationData = {
            email:email,
            otp: otp
            // email: localStorage.getItem('pendingVerificationEmail') || 'default@example.com' 
        };

        try {
            const response = await fetch(VERIFY_OTP_ENDPOINT, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(verificationData),
            });

            if (response.ok) {
                // OTP is correct! User is verified.
                console.log('Verification successful.');
                alert('Account verified successfully! You can now log in.');
                // Redirect user to the login page or home page
                navigate('/login'); 
            } else {
                // OTP is incorrect or expired
                const errorResult = await response.json();
                alert(`Verification failed: ${errorResult.message || 'Invalid OTP.'}`);
            }

        } catch (error) {
            console.error('Network error during OTP verification:', error);
            alert('A network error occurred.');
        }
    };

    return (
        <section className="flex flex-col items-center py-10">
            <h2 className="text-2xl font-bold mb-5">Verify Your Account</h2>
            <p className="text-gray-600 mb-7 text-center">
                We've sent a one-time password (OTP) to your email.
            </p>
            <form onSubmit={handleSubmit} className="flex flex-col gap-7 w-full max-w-sm">
                <input
                    type="text"
                    name="email"
                    id="email"
                    placeholder="Enter email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="px-7 py-3 rounded-xl bg-stone-100 text-center text-lg tracking-widest"
                    required
                />
                <input
                    type="text"
                    name="otp"
                    id="otp"
                    placeholder="Enter 6-digit OTP"
                    value={otp}
                    onChange={(e) => setOtp(e.target.value)}
                    maxLength="6"
                    className="px-7 py-3 rounded-xl bg-stone-100 text-center text-lg tracking-widest"
                    required
                />
                <button 
                    type="submit" 
                    className="px-7 py-3 rounded-xl text-white bg-blue-600 hover:bg-blue-700"
                >
                    Verify Account
                </button>
            </form>
        </section>
    );
}