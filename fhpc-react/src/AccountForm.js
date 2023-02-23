import { useState } from 'react';
import './App.css';

function BoostrapInput(props) {
    const {id, placeholder, labelText, value, onChange, type} = props;
    return (
        <div className="mb-3">
        <label htmlFor={id} className="form-label">{labelText}</label>
        <input onChange={onChange} required type={type} className="form-control" id={id} name={id} value={value} placeholder={placeholder} />
    </div>
    )
}

function AccountForm(props) {
    const [formData, setFormData] = useState({
        email: '',
        name: '',
        password: ''
    })

    const handleFormChange = (e) => {
        const value = e.target.value;
        const inputName = e.target.name;
        setFormData({
            ...formData,
            [inputName]: value
        })
    }

    return (
        <>
        <form className='form'>
            <BoostrapInput 
                id="email" 
                placeholder="emailaddress@email.com" 
                labelText="Email address"
                value={formData.email}
                onChange={handleFormChange}
                type="email" />
            <BoostrapInput 
                id="name" 
                placeholder="John Doe" 
                labelText="Name"
                value={formData.name}
                onChange={handleFormChange}
                type="text" />
            <BoostrapInput 
                id="password" 
                placeholder="Super Secret Password" 
                labelText="Password"
                value={formData.password}
                onChange={handleFormChange}
                type="text" />
            <button type="submit" className="btn btn-primary">Submit</button>
        </form>
        </>
    );
}

export default AccountForm;