import './App.css';
import Navbar from './components/Navbar';
import AccountForm from './AccountForm';
import LoginForm from "./Login"
import {BrowserRouter as Router} from 'react-router-dom'
import { useState } from 'react';
import Sidebar from './components/Sidebar';
import Home from './pages/index';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  return (
    <Router>
      <Home />
      <Navbar isLoggedIn={isLoggedIn} handleLogout={handleLogout}/>
        <AccountForm />
        <LoginForm setIsLoggedIn={setIsLoggedIn}/>
    </Router>
  );
}

export default App;
