
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Layout from './layouts/Layout'
import Home from './Home'
import Registration from './Registration'
import VerifyOtp from './VerifyOtp'
import Login from './Login'
import ResetPasswordVerify from './ResetPassword'
import Dashboard from './Daslhoard'
import DashboardLayout from './layouts/DashboardLayout'

function App() {
  

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Layout/>}>
            <Route index element={<Home/>}/>
            <Route path='/registration' element={<Registration/>}/>
            <Route path='/verify-otp' element={<VerifyOtp/>}/>
            <Route path='/login' element={<Login/>}/>
            <Route path='/reset-password-verify' element={<ResetPasswordVerify/>}/> 
          </Route>
          <Route path='/dashboard' element={<DashboardLayout/>}>
            <Route index element={<Dashboard/>}/>
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
