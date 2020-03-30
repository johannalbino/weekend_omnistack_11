import React, { useState } from 'react';
import { FiArrowLeft } from 'react-icons/fi';
import './styles.css';
import logo from '../../assets/logo.svg';
import { Link, useHistory } from 'react-router-dom';
import api from '../../services/api';

export default function Register(){

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [phone_number, setPhoneNumber] = useState('');
    const [city, setCity] = useState('');
    const [uf, setUf] = useState('');
    const [password, setPassword] = useState('');

    const history = useHistory();


    async function  handleRegister(e){
        e.preventDefault();

        const data ={
            username,
            email,
            phone_number,
            city,
            uf,
            password,
        };

        try {
            const response = await api.post('ong/', data);
            alert(`ONG criada com sucesso.`);
            history.push('/');
        } catch (err) {
            alert('Erro ao tentar cadastrar.')
        }
    }

    return (
        <div className="register-container">
            <div className="content">
                <section>
                    <img src={logo} alt="Be The hero" />

                    <h1>Cadastro</h1>
                    <p>Faça seu cadastro, entre na plataforma e ajude pessoas a encontrarem os casos da sua ONG.</p>
                    
                    <Link className="back-link" to="/">
                        <FiArrowLeft size={16} color="#E02041" /> Não tenho cadastro!
                    </Link>
                </section>
                
                <form onSubmit={handleRegister}>
                    <input 
                        placeholder="Nome da ONG" 
                        value={username} 
                        onChange={e => setUsername(e.target.value)} />
                    <input
                        placeholder="Sua senha"
                        value={password}
                        type="password"
                        onChange={e => setPassword(e.target.value)} />
                    <input type="email" 
                        placeholder="E-mail"
                        value={email}
                        onChange={e => setEmail(e.target.value)} />
                    <input 
                        placeholder="WhastApp"
                        value={phone_number} 
                        onChange={e => setPhoneNumber(e.target.value)}/>
                    <div className="input-group">
                        <input 
                            placeholder="Cidade" 
                            value={city}
                            onChange={e => setCity(e.target.value)} />
                        <input 
                            placeholder="UF" 
                            style={{ width: 80}}
                            value={uf}
                            onChange={e => setUf(e.target.value)} />
                    </div>
                    <button className="button" type="submit">Cadastrar</button>
                </form>
            </div>
        </div>
    )
}