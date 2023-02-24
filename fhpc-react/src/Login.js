import { useState } from 'react';
import Cookies from 'js-cookie';

function LoginInput(props) {
    const {id, placeholder, labelText, value, onChange, type} = props;
    return (
        <div className='mb-3'>
            <label htmlFor={id} className='form-label'>{labelText}</label>
            <input onChange={onChange} required type={type} className="form-control" id={id} name={id} value={value} placeholder={placeholder} />
        </div>
    )
}

export default function LoginForm(props) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const { setIsLoggedIn } = props;
  
    const handleUsernameChange = (event) => {
      setUsername(event.target.value);
    };
  
    const handlePasswordChange = (event) => {
      setPassword(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('http://localhost:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                password: password,
              }),
        });
        const data = await response.json()
        const accessToken = Cookies.get('access_token');
        setIsLoggedIn(true);
        Cookies.set('accessToken', data.access);
    }

    return (
        <>
        <form className='form' onSubmit={handleSubmit}>
            <LoginInput
                id="username"
                placeholder="username"
                labelText=" UserName"
                value={username}
                onChange={handleUsernameChange}
                type="text" />
            <LoginInput 
                id="password" 
                placeholder="Super Secret Password" 
                labelText="Password"
                value={password}
                onChange={handlePasswordChange}
                type="text" />
            <button type="submit" className="btn btn-primary">Login</button>
        </form>
        </>
    )
}